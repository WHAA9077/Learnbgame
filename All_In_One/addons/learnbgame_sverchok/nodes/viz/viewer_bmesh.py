# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# MK2

import itertools

import bpy
from bpy.props import BoolProperty, StringProperty, BoolVectorProperty
from mathutils import Matrix, Vector

from sverchok.node_tree import SverchCustomTreeNode
from sverchok.data_structure import dataCorrect, fullList, updateNode
from sverchok.utils.sv_bmesh_utils import bmesh_from_pydata
from sverchok.utils.sv_viewer_utils import (
    #matrix_sanitizer,
    natural_plus_one,
    greek_alphabet
)
from sverchok.utils.sv_obj_helper import SvObjHelper, CALLBACK_OP, get_random_init_v2


def default_mesh(name):
    # verts, faces = [(1, 1, -1), (1, -1, -1), (-1, -1, -1)], [(0, 1, 2)]
    mesh_data = bpy.data.meshes.new(name)
    # mesh_data.from_pydata(verts, [], faces)
    # mesh_data.update()
    return mesh_data


def make_bmesh_geometry(node, obj_index, context, verts, *topology):
    collection = context.scene.collection
    meshes = bpy.data.meshes
    objects = bpy.data.objects

    edges, faces, matrix = topology
    name = node.basedata_name + '.' + str("%04d" % obj_index)

    if name in objects:
        sv_object = objects[name]
    else:
        temp_mesh = default_mesh(name)
        sv_object = objects.new(name, temp_mesh)
        collection.objects.link(sv_object)

    # book-keeping via ID-props!? even this is can be broken by renames
    sv_object['idx'] = obj_index
    sv_object['madeby'] = node.name
    sv_object['basedata_name'] = node.basedata_name

    mesh = sv_object.data
    current_count = len(mesh.vertices)
    propose_count = len(verts)
    difference = (propose_count - current_count)

    ''' With this mode you make a massive assumption about the
        constant state of geometry. Assumes the count of verts
        edges/faces stays the same, and only updates the locations

        node.fixed_verts is not suitable for initial object creation
        but if over time you find that the only change is going to be
        vertices, this mode can be switched to to increase efficiency
    '''
    if node.fixed_verts and difference == 0:
        f_v = list(itertools.chain.from_iterable(verts))
        mesh.vertices.foreach_set('co', f_v)
        mesh.update()
    else:

        ''' get bmesh, write bmesh to obj, free bmesh'''
        bm = bmesh_from_pydata(verts, edges, faces, normal_update=node.calc_normals)
        bm.to_mesh(sv_object.data)
        bm.free()

        sv_object.hide_select = False

    if matrix:
        # matrix = matrix_sanitizer(matrix)
        if node.extended_matrix:
            sv_object.data.transform(matrix)
            sv_object.matrix_local = Matrix.Identity(4)
        else:
            sv_object.matrix_local = matrix
    else:
        sv_object.matrix_local = Matrix.Identity(4)


def make_bmesh_geometry_merged(node, obj_index, context, yielder_object):
    scene = context.scene
    collection = scene.collection
    meshes = bpy.data.meshes
    objects = bpy.data.objects
    name = node.basedata_name + '.' + str("%04d" % obj_index)

    if name in objects:
        sv_object = objects[name]
    else:
        temp_mesh = default_mesh(name)
        sv_object = objects.new(name, temp_mesh)
        collection.objects.link(sv_object)

    # book-keeping via ID-props!
    sv_object['idx'] = obj_index
    sv_object['madeby'] = node.name
    sv_object['basedata_name'] = node.basedata_name

    vert_count = 0
    big_verts = []
    big_edges = []
    big_faces = []

    for result in yielder_object:

        verts, topology = result
        edges, faces, matrix = topology

        if matrix:
            # matrix = matrix_sanitizer(matrix)
            verts = [matrix @ Vector(v) for v in verts]

        big_verts.extend(verts)
        big_edges.extend([[a + vert_count, b + vert_count] for a, b in edges])
        big_faces.extend([[j + vert_count for j in f] for f in faces])

        vert_count += len(verts)


    if node.fixed_verts and len(sv_object.data.vertices) == len(big_verts):
        mesh = sv_object.data
        f_v = list(itertools.chain.from_iterable(big_verts))
        mesh.vertices.foreach_set('co', f_v)
        mesh.update()
    else:
        ''' get bmesh, write bmesh to obj, free bmesh'''
        bm = bmesh_from_pydata(big_verts, big_edges, big_faces, normal_update=node.calc_normals)
        bm.to_mesh(sv_object.data)
        bm.free()

    sv_object.hide_select = False
    sv_object.matrix_local = Matrix.Identity(4)


class SvBmeshViewerNodeV28(bpy.types.Node, SverchCustomTreeNode, SvObjHelper):
    """ bmv Generate Live geom """

    bl_idname = 'SvBmeshViewerNodeV28'
    bl_label = 'Viewer BMesh'
    bl_icon = 'OUTLINER_OB_MESH'

    grouping: BoolProperty(default=False)
    merge: BoolProperty(default=False, update=updateNode)

    calc_normals: BoolProperty(default=False, update=updateNode)

    fixed_verts: BoolProperty(
        default=False,
        description="Use only with unchanging topology")

    autosmooth: BoolProperty(
        default=False,
        update=updateNode,
        description="This auto sets all faces to smooth shade")

    extended_matrix: BoolProperty(
        default=False,
        description='Allows mesh.transform(matrix) operation, quite fast!')

    def sv_init(self, context):
        self.sv_init_helper_basedata_name()

        self.inputs.new('VerticesSocket', 'vertices')
        self.inputs.new('StringsSocket', 'edges')
        self.inputs.new('StringsSocket', 'faces')
        self.inputs.new('MatrixSocket', 'matrix')

        self.outputs.new('SvObjectSocket', "Objects")

    def draw_buttons(self, context, layout):
        self.draw_live_and_outliner(context, layout)

        # additional UI options.
        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(self, "grouping", text="Group", toggle=True)
        row.prop(self, "merge", text="Merge", toggle=True)

        self.draw_object_buttons(context, layout)


    def draw_buttons_ext(self, context, layout):
        # self.draw_buttons(context, layout)
        self.draw_ext_object_buttons(context, layout)

        col = layout.column(align=True)
        box = col.box()
        if box:
            box.label(text="Beta options")
            box.prop(self, "extended_matrix", text="Extended Matrix")
            box.prop(self, "fixed_verts", text="Fixed vert count")
            box.prop(self, 'autosmooth', text='smooth shade')
            box.prop(self, 'calc_normals', text='calculate normals')
            box.prop(self, 'layer_choice', text='layer')

    def get_geometry_from_sockets(self):

        def get(socket_name):
            return self.inputs[socket_name].sv_get(default=[])

        mverts = get('vertices')
        medges = get('edges')
        mfaces = get('faces')
        mmtrix = get('matrix')
        return mverts, medges, mfaces, mmtrix

    def get_structure(self, stype, sindex):
        if not stype:
            return []

        try:
            j = stype[sindex]
        except IndexError:
            j = []
        finally:
            return j

    def process(self):

        if not self.activate:
            return

        mverts, *mrest = self.get_geometry_from_sockets()

        def get_edges_faces_matrices(obj_index):
            for geom in mrest:
                yield self.get_structure(geom, obj_index)

        # extend all non empty lists to longest of mverts or *mrest
        maxlen = max(len(mverts), *(map(len, mrest)))
        fullList(mverts, maxlen)
        for idx in range(3):
            if mrest[idx]:
                fullList(mrest[idx], maxlen)

        if self.merge:
            obj_index = 0

            def keep_yielding():
                # this will yield all in one go.
                for idx, Verts in enumerate(mverts):
                    if not Verts:
                        continue

                    data = get_edges_faces_matrices(idx)
                    yield (Verts, data)

            yielder_object = keep_yielding()
            make_bmesh_geometry_merged(self, obj_index, bpy.context, yielder_object)

        else:
            for obj_index, Verts in enumerate(mverts):
                if not Verts:
                    continue

                data = get_edges_faces_matrices(obj_index)
                make_bmesh_geometry(self, obj_index, bpy.context, Verts, *data)

        last_index = (len(mverts) - 1) if not self.merge else 0
        self.remove_non_updated_objects(last_index)

        objs = self.get_children()

        if self.grouping:
            self.to_group(objs)

        # truthy if self.material is in .materials
        if bpy.data.materials.get(self.material):
            self.set_corresponding_materials()

        if self.autosmooth:
            self.set_autosmooth(objs)

        if self.outputs[0].is_linked:
            self.outputs[0].sv_set(objs)


    def set_autosmooth(self, objs):
        for obj in objs:
            mesh = obj.data
            smooth_states = [True] * len(mesh.polygons)
            mesh.polygons.foreach_set('use_smooth', smooth_states)
            mesh.update()


    def add_material(self):

        mat = bpy.data.materials.new('sv_material')
        mat.use_nodes = True
        mat.use_fake_user = True

        nodes = mat.node_tree.nodes
        self.material = mat.name
        
        if bpy.context.scene.render.engine == 'CYCLES':
            # add attr node to the left of diffuse BSDF + connect it
            diffuse_node = nodes['Diffuse BSDF']
            attr_node = nodes.new('ShaderNodeAttribute')
            attr_node.location = (-170, 300)
            attr_node.attribute_name = 'SvCol'

            links = mat.node_tree.links
            links.new(attr_node.outputs[0], diffuse_node.inputs[0])        


def register():
    bpy.utils.register_class(SvBmeshViewerNodeV28)



def unregister():
    bpy.utils.unregister_class(SvBmeshViewerNodeV28)
