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

# <pep8-80 compliant>

bl_info = {
    "name": "Wavefront OBJ format (sge version)",
    "author": "Campbell Barton, Niels Meyering, Philipp Middendorf",
    "blender": (2, 6, 3),
    "location": "File > Import-Export",
    "description": "Import-Export OBJ, Import OBJ mesh, UV's, "
                   "materials and textures (sge style)",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.5/Py/"
                "Scripts/Import-Export/Wavefront_OBJ",
    "tracker_url": "",
    "support": 'OFFICIAL',
    "category": "Learnbgame",
}

if "bpy" in locals():
    import imp
    if "import_obj" in locals():
        imp.reload(import_obj)
    if "export_obj" in locals():
        imp.reload(export_obj)


import bpy
from bpy.props import (BoolProperty,
                       FloatProperty,
                       StringProperty,
                       EnumProperty,
                       )
from bpy_extras.io_utils import (ExportHelper,
                                 ImportHelper,
                                 path_reference_mode,
                                 axis_conversion,
                                 )


class ImportOBJ(bpy.types.Operator, ImportHelper):
    '''Load a Wavefront OBJ File'''
    bl_idname = "import_scene.obj"
    bl_label = "Import OBJ"
    bl_options = {'PRESET', 'UNDO'}

    filename_ext = ".obj"
    filter_glob = StringProperty(
            default="*.obj;*.mtl",
            options={'HIDDEN'},
            )

    use_ngons = BoolProperty(
            name="NGons",
            description="Import faces with more than 4 verts as fgons",
            default=True,
            )
    use_edges = BoolProperty(
            name="Lines",
            description="Import lines and faces with 2 verts as edge",
            default=True,
            )
    use_smooth_groups = BoolProperty(
            name="Smooth Groups",
            description="Surround smooth groups by sharp edges",
            default=True,
            )

    use_split_objects = BoolProperty(
            name="Object",
            description="Import OBJ Objects into Blender Objects",
            default=True,
            )
    use_split_groups = BoolProperty(
            name="Group",
            description="Import OBJ Groups into Blender Objects",
            default=True,
            )

    use_groups_as_vgroups = BoolProperty(
            name="Poly Groups",
            description="Import OBJ groups as vertex groups",
            default=False,
            )

    use_image_search = BoolProperty(
            name="Image Search",
            description="Search subdirs for any assosiated images " \
                        "(Warning, may be slow)",
            default=True,
            )

    split_mode = EnumProperty(
            name="Split",
            items=(('ON', "Split", "Split geometry, omits unused verts"),
                   ('OFF', "Keep Vert Order", "Keep vertex order from file"),
                   ),
            )

    global_clamp_size = FloatProperty(
            name="Clamp Scale",
            description="Clamp the size to this maximum (Zero to Disable)",
            min=0.0, max=1000.0,
            soft_min=0.0, soft_max=1000.0,
            default=0.0,
            )
    axis_forward = EnumProperty(
            name="Forward",
            items=(('X', "X Forward", ""),
                   ('Y', "Y Forward", ""),
                   ('Z', "Z Forward", ""),
                   ('-X', "-X Forward", ""),
                   ('-Y', "-Y Forward", ""),
                   ('-Z', "-Z Forward", ""),
                   ),
            default='-Z',
            )

    axis_up = EnumProperty(
            name="Up",
            items=(('X', "X Up", ""),
                   ('Y', "Y Up", ""),
                   ('Z', "Z Up", ""),
                   ('-X', "-X Up", ""),
                   ('-Y', "-Y Up", ""),
                   ('-Z', "-Z Up", ""),
                   ),
            default='Y',
            )

    def execute(self, context):
        # print("Selected: " + context.active_object.name)
        from . import import_obj

        if self.split_mode == 'OFF':
            self.use_split_objects = False
            self.use_split_groups = False
        else:
            self.use_groups_as_vgroups = False

        keywords = self.as_keywords(ignore=("axis_forward",
                                            "axis_up",
                                            "filter_glob",
                                            "split_mode",
                                            ))

        global_matrix = axis_conversion(from_forward=self.axis_forward,
                                        from_up=self.axis_up,
                                        ).to_4x4()
        keywords["global_matrix"] = global_matrix

        return import_obj.load(self, context, **keywords)

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)
        row.prop(self, "use_ngons")
        row.prop(self, "use_edges")

        layout.prop(self, "use_smooth_groups")

        box = layout.box()
        row = box.row()
        row.prop(self, "split_mode", expand=True)

        row = box.row()
        if self.split_mode == 'ON':
            row.label(text="Split by:")
            row.prop(self, "use_split_objects")
            row.prop(self, "use_split_groups")
        else:
            row.prop(self, "use_groups_as_vgroups")

        row = layout.split(percentage=0.67)
        row.prop(self, "global_clamp_size")
        layout.prop(self, "axis_forward")
        layout.prop(self, "axis_up")

        layout.prop(self, "use_image_search")


class ExportOBJ(bpy.types.Operator, ExportHelper):
    '''Save a Wavefront OBJ File'''

    bl_idname = "export_scene.obj"
    bl_label = 'Export OBJ'
    bl_options = {'PRESET'}

    filename_ext = ".obj"
    filter_glob = StringProperty(
            default="*.obj;*.mtl",
            options={'HIDDEN'},
            )

    # context group
    use_selection = BoolProperty(
            name="Selection Only",
            description="Export selected objects only",
            default=True,
            )
    use_animation = BoolProperty(
            name="Animation",
            description="Write out an OBJ for each frame",
            default=False,
            )

    # object group
    use_apply_modifiers = BoolProperty(
            name="Apply Modifiers",
            description="Apply modifiers (preview resolution)",
            default=True,
            )

    # extra data group
    use_edges = BoolProperty(
            name="Include Edges",
            description="",
            default=True,
            )
    use_normals = BoolProperty(
            name="Include Normals",
            description="",
            default=True,
            )
    use_uvs = BoolProperty(
            name="Include UVs",
            description="Write out the active UV coordinates",
            default=True,
            )
    use_materials = BoolProperty(
            name="Write Materials",
            description="Write out the MTL file",
            default=True,
            )
    use_triangles = BoolProperty(
            name="Triangulate Faces",
            description="Convert all faces to triangles",
            default=True,
            )
    use_nurbs = BoolProperty(
            name="Write Nurbs",
            description="Write nurbs curves as OBJ nurbs rather than "
                        "converting to geometry",
            default=False,
            )
    use_vertex_groups = BoolProperty(
            name="Polygroups",
            description="",
            default=False,
            )

    # grouping group
    use_blen_objects = BoolProperty(
            name="Objects as OBJ Objects",
            description="",
            default=True,
            )
    group_by_object = BoolProperty(
            name="Objects as OBJ Groups ",
            description="",
            default=False,
            )
    group_by_material = BoolProperty(
            name="Material Groups",
            description="",
            default=False,
            )
    keep_vertex_order = BoolProperty(
            name="Keep Vertex Order",
            description="",
            default=False,
            )

    global_scale = FloatProperty(
            name="Scale",
            description="Scale all data",
            min=0.01, max=1000.0,
            soft_min=0.01,
            soft_max=1000.0,
            default=1.0,
            )

    axis_forward = EnumProperty(
            name="Forward",
            items=(('X', "X Forward", ""),
                   ('Y', "Y Forward", ""),
                   ('Z', "Z Forward", ""),
                   ('-X', "-X Forward", ""),
                   ('-Y', "-Y Forward", ""),
                   ('-Z', "-Z Forward", ""),
                   ),
            default='-Z',
            )

    axis_up = EnumProperty(
            name="Up",
            items=(('X', "X Up", ""),
                   ('Y', "Y Up", ""),
                   ('Z', "Z Up", ""),
                   ('-X', "-X Up", ""),
                   ('-Y', "-Y Up", ""),
                   ('-Z', "-Z Up", ""),
                   ),
            default='Y',
            )

    path_mode = path_reference_mode

    check_extension = True

    def execute(self, context):
        from . import export_obj

        from mathutils import Matrix
        keywords = self.as_keywords(ignore=("axis_forward",
                                            "axis_up",
                                            "global_scale",
                                            "check_existing",
                                            "filter_glob",
                                            ))

        global_matrix = Matrix()

        global_matrix[0][0] = \
        global_matrix[1][1] = \
        global_matrix[2][2] = self.global_scale

        global_matrix = (global_matrix *
                         axis_conversion(to_forward=self.axis_forward,
                                         to_up=self.axis_up,
                                         ).to_4x4())

        keywords["global_matrix"] = global_matrix
        return export_obj.save(self, context, **keywords)


def menu_func_import(self, context):
    self.layout.operator(ImportOBJ.bl_idname, text="Wavefront (.obj)")


def menu_func_export(self, context):
    self.layout.operator(ExportOBJ.bl_idname, text="Wavefront (.obj)")


def register():
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_file_import.append(menu_func_import)
    bpy.types.INFO_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_file_import.remove(menu_func_import)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()
