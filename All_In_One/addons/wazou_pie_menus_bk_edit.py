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

bl_info = {
    "name": "Wazou Pie Menus bk.Edit",
    "author": "Bookyakuno & Cédric Lepiller & DavideDozza & Lapineige & Leafar & 0rAngE",
    "version": (0, 2, 1),
    "blender": (2, 79, 0),
    "description": "Custom Pie Menus",
    "category": "Learnbgame",
}

import bpy, os
from bpy.types import Menu, Header
from bpy.props import IntProperty, FloatProperty, BoolProperty
import bmesh
from mathutils import *
import math

class WazouPieMenuPrefs(bpy.types.AddonPreferences):
    """Creates the tools in a Panel, in the scene context of the properties editor"""
    bl_idname = __name__

    bpy.types.Scene.Enable_Tab_01 = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.Enable_Tab_02 = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.Enable_Tab_03 = bpy.props.BoolProperty(default=False)

    def draw(self, context):
        layout = self.layout

        layout.prop(context.scene, "Enable_Tab_01", text="Info", icon="QUESTION")
        if context.scene.Enable_Tab_01:
            row = layout.row()
            layout.label(text="This Addon Need to activate 'Loop Tools' and 'Bsurfaces' in the Addon Tab to work properly.")
            layout.label(text="You need to install Iceking's Tool And Auto Mirror")

            layout.operator("wm.url_open", text="IceKing's tools").url = "http://www.blenderartists.org/forum/showthread.php?343641-Iceking-s-Tools"
            layout.operator("wm.url_open", text="Auto Mirror").url = "http://le-terrier-de-lapineige.over-blog.com/2014/07/automirror-mon-add-on-pour-symetriser-vos-objets-rapidement.html"

        layout.prop(context.scene, "Enable_Tab_02", text="Shortcuts", icon="QUESTION")
        if context.scene.Enable_Tab_02:



            layout = self.layout
            scene = context.scene
            cscene = scene.cycles
            rd = context.scene.render



            col = layout.column(align=True)


            # col = split.column()
            row = col.row(align=True)
            row.label(text="– Object/Edit mode & Vertex/Edge/face >", icon='FACESEL')
            row.label(text="Right mouse")

            split = layout.split()
            row = col.row(align=True)
            row.label(text="– Pivot point   >", icon='ROTATECOLLECTION')
            row.label(text="Right mouse + alt")

            split = layout.split()
            row = col.row(align=True)
            row.label(text="– Shading >", icon='MATERIAL')
            row.label(text="Right mouse + alt + shift")

            split = layout.split()
            row = col.row(align=True)
            row.label(text="– Views >", icon='NODETREE')
            row.label(text="Ctrl + Q")

            split = layout.split()
            row = col.row(align=True)
            row.label(text="– Cursor/Origin >", icon='CURSOR')
            row.label(text="Shift + S")

            split = layout.split()
            row = col.row(align=True)
            row.label(text="– Selections >", icon='BORDER_RECT')
            row.label(text="Shift + G")




        layout.prop(context.scene, "Enable_Tab_03", text="URL's", icon="URL")
        if context.scene.Enable_Tab_03:
            row = layout.row()
            row.operator("wm.url_open", text="Pitiwazou.com").url = "http://www.pitiwazou.com/"
            row.operator("wm.url_open", text="Wazou's Ghitub").url = "https://github.com/pitiwazou/Scripts-Blender"
            row.operator("wm.url_open", text="BlenderLounge Forum ").url = "http://blenderlounge.fr/forum/"
            row = layout.row()
            row.operator("wm.url_open", text="bookyakuno github").url = "https://github.com/bookyakuno/-Blender-/tree/0a0e3bd36e87aa3fabd8f39839f9abbffe7ec665"



class add_nurbs_curves(bpy.types.Operator):
    bl_idname = "object.add_nurbs_curves"
    bl_label = "add_nurbs_curves"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        bpy.context.object.data.resolution_u = 3
        bpy.context.object.data.bevel_resolution = 2
        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_depth = 0.254
        bpy.ops.object.shade_flat()
        bpy.ops.shading.flat()

        return {'FINISHED'}



class WireAll(bpy.types.Operator):
    bl_idname = "object.wireall"
    bl_label = "Wire All"

    def execute(self, context):

        for obj in bpy.data.objects:
            if obj.show_wire:
                obj.show_all_edges = False #すべてのエッジを非表示
                obj.show_wire = False#ワイヤーフレーム表示がオフの場合
            else:
                obj.show_all_edges = True
                obj.show_wire = True
        return {'FINISHED'}








#####################################
#      Proportional Edit Object     #
#####################################
class ProportionalEditObj(bpy.types.Operator):
    bl_idname = "proportional_obj.active"
    bl_label = "Proportional Edit Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.scene.tool_settings.use_proportional_edit_objects == (True):
            bpy.context.scene.tool_settings.use_proportional_edit_objects = False

        elif bpy.context.scene.tool_settings.use_proportional_edit_objects == (False) :
             bpy.context.scene.tool_settings.use_proportional_edit_objects = True

        return {'FINISHED'}

class ProportionalSmoothObj(bpy.types.Operator):
    bl_idname = "proportional_obj.smooth"
    bl_label = "Proportional Smooth Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_proportional_edit_objects == (False) :
            bpy.context.scene.tool_settings.use_proportional_edit_objects = True
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SMOOTH'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'SMOOTH':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SMOOTH'
        return {'FINISHED'}

class ProportionalSphereObj(bpy.types.Operator):
    bl_idname = "proportional_obj.sphere"
    bl_label = "Proportional Sphere Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_proportional_edit_objects == (False) :
            bpy.context.scene.tool_settings.use_proportional_edit_objects = True
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SPHERE'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'SPHERE':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SPHERE'
        return {'FINISHED'}

class ProportionalRootObj(bpy.types.Operator):
    bl_idname = "proportional_obj.root"
    bl_label = "Proportional Root Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_proportional_edit_objects == (False) :
            bpy.context.scene.tool_settings.use_proportional_edit_objects = True
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'ROOT'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'ROOT':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'ROOT'
        return {'FINISHED'}

class ProportionalSharpObj(bpy.types.Operator):
    bl_idname = "proportional_obj.sharp"
    bl_label = "Proportional Sharp Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_proportional_edit_objects == (False) :
            bpy.context.scene.tool_settings.use_proportional_edit_objects = True
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SHARP'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'SHARP':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SHARP'
        return {'FINISHED'}

class ProportionalLinearObj(bpy.types.Operator):
    bl_idname = "proportional_obj.linear"
    bl_label = "Proportional Linear Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_proportional_edit_objects == (False) :
            bpy.context.scene.tool_settings.use_proportional_edit_objects = True
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'LINEAR'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'LINEAR':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'LINEAR'
        return {'FINISHED'}

class ProportionalConstantObj(bpy.types.Operator):
    bl_idname = "proportional_obj.constant"
    bl_label = "Proportional Constant Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_proportional_edit_objects == (False) :
            bpy.context.scene.tool_settings.use_proportional_edit_objects = True
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'CONSTANT'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'CONSTANT':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'CONSTANT'
        return {'FINISHED'}

class ProportionalRandomObj(bpy.types.Operator):
    bl_idname = "proportional_obj.random"
    bl_label = "Proportional Random Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_proportional_edit_objects == (False) :
            bpy.context.scene.tool_settings.use_proportional_edit_objects = True
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'RANDOM'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'RANDOM':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'RANDOM'
        return {'FINISHED'}

#######################################
#     Proportional Edit Edit Mode     #
#######################################
class ProportionalEditEdt(bpy.types.Operator):
    bl_idname = "proportional_edt.active"
    bl_label = "Proportional Edit EditMode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.scene.tool_settings.proportional_edit != ('DISABLED'):
            bpy.context.scene.tool_settings.proportional_edit = 'DISABLED'
        elif bpy.context.scene.tool_settings.proportional_edit != ('ENABLED'):
            bpy.context.scene.tool_settings.proportional_edit = 'ENABLED'
        return {'FINISHED'}

class ProportionalConnectedEdt(bpy.types.Operator):
    bl_idname = "proportional_edt.connected"
    bl_label = "Proportional Connected EditMode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.scene.tool_settings.proportional_edit != ('CONNECTED'):
            bpy.context.scene.tool_settings.proportional_edit = 'CONNECTED'
        return {'FINISHED'}

class ProportionalProjectedEdt(bpy.types.Operator):
    bl_idname = "proportional_edt.projected"
    bl_label = "Proportional projected EditMode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.scene.tool_settings.proportional_edit != ('PROJECTED'):
            bpy.context.scene.tool_settings.proportional_edit = 'PROJECTED'
        return {'FINISHED'}

class ProportionalSmoothEdt(bpy.types.Operator):
    bl_idname = "proportional_edt.smooth"
    bl_label = "Proportional Smooth EditMode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.proportional_edit == ('DISABLED') :
            bpy.context.scene.tool_settings.proportional_edit = 'ENABLED'
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SMOOTH'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'SMOOTH':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SMOOTH'
        return {'FINISHED'}

class ProportionalSphereEdt(bpy.types.Operator):
    bl_idname = "proportional_edt.sphere"
    bl_label = "Proportional Sphere EditMode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.proportional_edit == ('DISABLED') :
            bpy.context.scene.tool_settings.proportional_edit = 'ENABLED'
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SPHERE'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'SPHERE':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SPHERE'
        return {'FINISHED'}

class ProportionalRootEdt(bpy.types.Operator):
    bl_idname = "proportional_edt.root"
    bl_label = "Proportional Root EditMode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.proportional_edit == ('DISABLED') :
            bpy.context.scene.tool_settings.proportional_edit = 'ENABLED'
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'ROOT'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'ROOT':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'ROOT'
        return {'FINISHED'}

class ProportionalSharpEdt(bpy.types.Operator):
    bl_idname = "proportional_edt.sharp"
    bl_label = "Proportional Sharp EditMode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.proportional_edit == ('DISABLED') :
            bpy.context.scene.tool_settings.proportional_edit = 'ENABLED'
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SHARP'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'SHARP':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SHARP'
        return {'FINISHED'}

class ProportionalLinearEdt(bpy.types.Operator):
    bl_idname = "proportional_edt.linear"
    bl_label = "Proportional Linear EditMode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.proportional_edit == ('DISABLED') :
            bpy.context.scene.tool_settings.proportional_edit = 'ENABLED'
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'LINEAR'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'LINEAR':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'LINEAR'
        return {'FINISHED'}

class ProportionalConstantEdt(bpy.types.Operator):
    bl_idname = "proportional_edt.constant"
    bl_label = "Proportional Constant EditMode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.proportional_edit == ('DISABLED') :
            bpy.context.scene.tool_settings.proportional_edit = 'ENABLED'
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'CONSTANT'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'CONSTANT':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'CONSTANT'
        return {'FINISHED'}

class ProportionalRandomEdt(bpy.types.Operator):
    bl_idname = "proportional_edt.random"
    bl_label = "Proportional Random EditMode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.proportional_edit == ('DISABLED') :
            bpy.context.scene.tool_settings.proportional_edit = 'ENABLED'
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'RANDOM'

        if bpy.context.scene.tool_settings.proportional_edit_falloff != 'RANDOM':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'RANDOM'
        return {'FINISHED'}

######################
#      Snapping      #
######################
class SnapActive(bpy.types.Operator):
    bl_idname = "snap.active"
    bl_label = "Snap Active"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.scene.tool_settings.use_snap == (True):
            bpy.context.scene.tool_settings.use_snap = False

        elif bpy.context.scene.tool_settings.use_snap == (False) :
             bpy.context.scene.tool_settings.use_snap = True

        return {'FINISHED'}


class SnapVolume(bpy.types.Operator):
    bl_idname = "snap.volume"
    bl_label = "Snap Volume"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_snap == (False) :
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VOLUME'

        if bpy.context.scene.tool_settings.snap_element != 'VOLUME':
            bpy.context.scene.tool_settings.snap_element = 'VOLUME'
        return {'FINISHED'}

class SnapFace(bpy.types.Operator):
    bl_idname = "snap.face"
    bl_label = "Snap Face"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_snap == (False) :
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'FACE'

        if bpy.context.scene.tool_settings.snap_element != 'FACE':
            bpy.context.scene.tool_settings.snap_element = 'FACE'
        return {'FINISHED'}

class SnapEdge(bpy.types.Operator):
    bl_idname = "snap.edge"
    bl_label = "Snap Edge"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_snap == (False) :
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'EDGE'

        if bpy.context.scene.tool_settings.snap_element != 'EDGE':
            bpy.context.scene.tool_settings.snap_element = 'EDGE'
        return {'FINISHED'}

class SnapVertex(bpy.types.Operator):
    bl_idname = "snap.vertex"
    bl_label = "Snap Vertex"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_snap == (False) :
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'

        if bpy.context.scene.tool_settings.snap_element != 'VERTEX':
            bpy.context.scene.tool_settings.snap_element = 'VERTEX'
        return {'FINISHED'}

class SnapIncrement(bpy.types.Operator):
    bl_idname = "snap.increment"
    bl_label = "Snap Increment"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_snap == (False) :
            bpy.context.scene.tool_settings.use_snap = True
            bpy.context.scene.tool_settings.snap_element = 'INCREMENT'

        if bpy.context.scene.tool_settings.snap_element != 'INCREMENT':
            bpy.context.scene.tool_settings.snap_element = 'INCREMENT'
        return {'FINISHED'}

class SnapAlignRotation(bpy.types.Operator):
    bl_idname = "snap.alignrotation"
    bl_label = "Snap Align rotation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.scene.tool_settings.use_snap_align_rotation == (True) :
            bpy.context.scene.tool_settings.use_snap_align_rotation = False

        elif bpy.context.scene.tool_settings.use_snap_align_rotation == (False) :
             bpy.context.scene.tool_settings.use_snap_align_rotation = True

        return {'FINISHED'}

class SnapTargetVariable(bpy.types.Operator):
    bl_idname = "object.snaptargetvariable"
    bl_label = "Snap Target Variable"
    bl_options = {'REGISTER', 'UNDO'}
    variable = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_target=self.variable
        return {'FINISHED'}

######################
#    Orientation     #
######################

class OrientationVariable(bpy.types.Operator):
    bl_idname = "object.orientationvariable"
    bl_label = "Orientation Variable"
    bl_options = {'REGISTER', 'UNDO'}
    variable = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.context.space_data.transform_orientation=self.variable
        return {'FINISHED'}

######################
#      Shading       #
######################

class ShadingVariable(bpy.types.Operator):
    bl_idname = "object.shadingvariable"
    bl_label = "Shading Variable"
    bl_options = {'REGISTER', 'UNDO'}
    variable = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.context.space_data.viewport_shade=self.variable
        return {'FINISHED'}

class ShadingSmooth(bpy.types.Operator):
    bl_idname = "shading.smooth"
    bl_label = "Shading Smooth"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.mode == "OBJECT":
            bpy.ops.object.shade_smooth()

        elif bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.shade_smooth()
            bpy.ops.object.mode_set(mode = 'EDIT')
        return {'FINISHED'}

class ShadingFlat(bpy.types.Operator):
    bl_idname = "shading.flat"
    bl_label = "Shading Flat"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.mode == "OBJECT":
            bpy.ops.object.shade_flat()

        elif bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.shade_flat()
            bpy.ops.object.mode_set(mode = 'EDIT')
        return {'FINISHED'}

######################
#   Object shading   #
######################

#Wire on selected objects
class WireSelectedAll(bpy.types.Operator):
    bl_idname = "wire.selectedall"
    bl_label = "Wire Selected All"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        for obj in bpy.data.objects:
            if bpy.context.selected_objects:
                if obj.select:
                    if obj.show_wire:
                        obj.show_all_edges = False
                        obj.show_wire = False
                    else:
                        obj.show_all_edges = True
                        obj.show_wire = True
            elif not bpy.context.selected_objects:
                if obj.show_wire:
                    obj.show_all_edges = False
                    obj.show_wire = False
                else:
                    obj.show_all_edges = True
                    obj.show_wire = True
        return {'FINISHED'}

#Grid show/hide with axes
class ToggleGridAxis(bpy.types.Operator):
    bl_idname = "scene.togglegridaxis"
    bl_label = "Toggle Grid and Axis in 3D view"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.space_data.show_axis_y = not bpy.context.space_data.show_axis_y
        bpy.context.space_data.show_axis_x = not bpy.context.space_data.show_axis_x
        bpy.context.space_data.show_floor = not bpy.context.space_data.show_floor
        return {'FINISHED'}

#Overlays
class MeshDisplayOverlays(bpy.types.Menu):
    bl_idname = "meshdisplay.overlays"
    bl_label = "Mesh Display Overlays"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout

        layout.operator("wm.context_toggle", text="Show Faces", icon='FACESEL').data_path = "object.data.show_faces"
        layout.operator("wm.context_toggle", text="Show Edges", icon='FACESEL').data_path = "object.data.show_edges"
        layout.operator("wm.context_toggle", text="Show Crease", icon='FACESEL').data_path = "object.data.show_edge_crease"
        layout.operator("wm.context_toggle", text="Show Seams", icon='FACESEL').data_path = "object.data.show_edge_seams"
        layout.operator("wm.context_toggle", text="Show Sharp", icon='FACESEL').data_path = "object.data.show_edge_sharp"
        layout.operator("wm.context_toggle", text="Show Bevel", icon='FACESEL').data_path = "object.data.show_edge_bevel_weight"
        layout.operator("wm.context_toggle", text="Show Edges Marks", icon='FACESEL').data_path = "object.data.show_freestyle_edge_marks"
        layout.operator("wm.context_toggle", text="Show Face Marks", icon='FACESEL').data_path = "object.data.show_freestyle_face_marks"
        layout.operator("wm.context_toggle", text="Show Weight", icon='FACESEL').data_path = "object.data.show_weight"

#auto smooth Menu
class AutoSmoothMenu(bpy.types.Menu):
    bl_idname = "auto.smooth_menu"
    bl_label = "Auto Smooth"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout
        layout.operator("wm.context_toggle", text="Auto Smooth", icon='MESH_DATA').data_path = "object.data.use_auto_smooth"
        layout.operator("auto.smooth_30", text="Auto Smooth 30", icon='MESH_DATA')
        layout.operator("auto.smooth_45", text="Auto Smooth 45", icon='MESH_DATA')
        layout.operator("auto.smooth_89", text="Auto Smooth 89", icon='MESH_DATA')

#AutoSmooth_89
class AutoSmooth89(bpy.types.Operator):
    bl_idname = "auto.smooth_89"
    bl_label = "Auto Smooth"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.context.object.data.auto_smooth_angle = 1.55334
        return {'FINISHED'}

#AutoSmooth_30
class AutoSmooth30(bpy.types.Operator):
    bl_idname = "auto.smooth_30"
    bl_label = "Auto Smooth"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.context.object.data.auto_smooth_angle = 0.523599
        return {'FINISHED'}

#AutoSmooth_45
class AutoSmooth45(bpy.types.Operator):
    bl_idname = "auto.smooth_45"
    bl_label = "Auto Smooth"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.context.object.data.auto_smooth_angle = 0.785398
        return {'FINISHED'}

#Normals
class NormalsMenu(bpy.types.Menu):
    bl_idname = "normals.menu"
    bl_label = "Normals Menu"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout
        layout.operator("wm.context_toggle", text="Show Normals Vertex", icon='MESH_DATA').data_path = "object.data.show_normal_vertex"
        layout.operator("wm.context_toggle", text="Show Normals Loop", icon='MESH_DATA').data_path = "object.data.show_normal_vertex"
        layout.operator("normalsize.01", text="Normal Size 01")
        layout.operator("normalsize.02", text="Normal Size 02")

#Normal Size 01
class NormalSize01(bpy.types.Operator):
    bl_idname = "normalsize.01"
    bl_label = "Normal Size 01"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.context.scene.tool_settings.normal_size = 0.1
        return {'FINISHED'}

#Normal Size 02
class NormalSize02(bpy.types.Operator):
    bl_idname = "normalsize.02"
    bl_label = "Normal Size 02"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.context.scene.tool_settings.normal_size = 0.2
        return {'FINISHED'}
######################
#    Pivot Point     #
######################

class PivotPointVariable(bpy.types.Operator):
    bl_idname = "pivotpoint.variable"
    bl_label = "PivotPointVariable"
    bl_options = {'REGISTER', 'UNDO'}
    variable = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.context.space_data.pivot_point = self.variable
        return {'FINISHED'}


class UsePivotAlign(bpy.types.Operator):
    bl_idname = "use.pivotalign"
    bl_label = "Use Pivot Align"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if bpy.context.space_data.use_pivot_point_align == (False) :
            bpy.context.space_data.use_pivot_point_align = True
        elif bpy.context.space_data.use_pivot_point_align == (True) :
             bpy.context.space_data.use_pivot_point_align = False
        return {'FINISHED'}

######################
#    Manipulators    #
######################
class ManipTranslate(bpy.types.Operator):
    bl_idname = "manip.translate"
    bl_label = "Manip Translate"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.space_data.show_manipulator == (False) :
            bpy.context.space_data.show_manipulator = True
            bpy.context.space_data.transform_manipulators = {'TRANSLATE'}
        if bpy.context.space_data.transform_manipulators != {'TRANSLATE'}:
            bpy.context.space_data.transform_manipulators = {'TRANSLATE'}
        return {'FINISHED'}

class ManipRotate(bpy.types.Operator):
    bl_idname = "manip.rotate"
    bl_label = "Manip Rotate"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.space_data.show_manipulator == (False) :
            bpy.context.space_data.show_manipulator = True
            bpy.context.space_data.transform_manipulators = {'ROTATE'}
        if bpy.context.space_data.transform_manipulators != {'ROTATE'}:
            bpy.context.space_data.transform_manipulators = {'ROTATE'}
        return {'FINISHED'}

class ManipScale(bpy.types.Operator):
    bl_idname = "manip.scale"
    bl_label = "Manip Scale"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.space_data.show_manipulator == (False) :
            bpy.context.space_data.show_manipulator = True
            bpy.context.space_data.transform_manipulators = {'SCALE'}
        if bpy.context.space_data.transform_manipulators != {'SCALE'}:
            bpy.context.space_data.transform_manipulators = {'SCALE'}
        return {'FINISHED'}

class TranslateRotate(bpy.types.Operator):
    bl_idname = "translate.rotate"
    bl_label = "Translate Rotate"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.space_data.show_manipulator == (False) :
            bpy.context.space_data.show_manipulator = True
            bpy.context.space_data.transform_manipulators = {'TRANSLATE', 'ROTATE'}
        if bpy.context.space_data.transform_manipulators != {'TRANSLATE', 'ROTATE'}:
            bpy.context.space_data.transform_manipulators = {'TRANSLATE', 'ROTATE'}
        return {'FINISHED'}

class TranslateScale(bpy.types.Operator):
    bl_idname = "translate.scale"
    bl_label = "Translate Scale"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.space_data.show_manipulator == (False) :
            bpy.context.space_data.show_manipulator = True
            bpy.context.space_data.transform_manipulators = {'TRANSLATE', 'SCALE'}
        if bpy.context.space_data.transform_manipulators != {'TRANSLATE', 'SCALE'}:
            bpy.context.space_data.transform_manipulators = {'TRANSLATE', 'SCALE'}
        return {'FINISHED'}

class RotateScale(bpy.types.Operator):
    bl_idname = "rotate.scale"
    bl_label = "Rotate Scale"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.space_data.show_manipulator == (False) :
            bpy.context.space_data.show_manipulator = True
            bpy.context.space_data.transform_manipulators = {'ROTATE', 'SCALE'}
        if bpy.context.space_data.transform_manipulators != {'ROTATE', 'SCALE'}:
            bpy.context.space_data.transform_manipulators = {'ROTATE', 'SCALE'}
        return {'FINISHED'}

class TranslateRotateScale(bpy.types.Operator):
    bl_idname = "translate.rotatescale"
    bl_label = "Translate Rotate Scale"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.space_data.show_manipulator == (False) :
            bpy.context.space_data.show_manipulator = True
            bpy.context.space_data.transform_manipulators = {'TRANSLATE', 'ROTATE', 'SCALE'}
        if bpy.context.space_data.transform_manipulators != {'TRANSLATE', 'ROTATE', 'SCALE'}:
            bpy.context.space_data.transform_manipulators = {'TRANSLATE', 'ROTATE', 'SCALE'}
        return {'FINISHED'}

class WManupulators(bpy.types.Operator):
    bl_idname = "w.manupulators"
    bl_label = "W Manupulators"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.space_data.show_manipulator == (True):
            bpy.context.space_data.show_manipulator = False

        elif bpy.context.space_data.show_manipulator == (False):
             bpy.context.space_data.show_manipulator = True

        return {'FINISHED'}

######################
#       Modes        #
######################

# Define Class Texture Paint
class ClassTexturePaint(bpy.types.Operator):
    bl_idname = "class.pietexturepaint"
    bl_label = "Class Texture Paint"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.paint.texture_paint_toggle()
        else:
            bpy.ops.paint.texture_paint_toggle()
        return {'FINISHED'}

# Define Class Weight Paint
class ClassWeightPaint(bpy.types.Operator):
    bl_idname = "class.pieweightpaint"
    bl_label = "Class Weight Paint"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.paint.weight_paint_toggle()
        else:
            bpy.ops.paint.weight_paint_toggle()
        return {'FINISHED'}

# Define Class Vertex Paint
class ClassVertexPaint(bpy.types.Operator):
    bl_idname = "class.pievertexpaint"
    bl_label = "Class Vertex Paint"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.paint.vertex_paint_toggle()
        else:
            bpy.ops.paint.vertex_paint_toggle()
        return {'FINISHED'}

# Define Class Particle Edit
class ClassParticleEdit(bpy.types.Operator):
    bl_idname = "class.pieparticleedit"
    bl_label = "Class Particle Edit"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.particle.particle_edit_toggle()
        else:
            bpy.ops.particle.particle_edit_toggle()

        return {'FINISHED'}

# Define Class Object Mode
class ClassObject(bpy.types.Operator):
    bl_idname = "class.object"
    bl_label = "Class Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode == "OBJECT":
            bpy.ops.object.mode_set(mode="EDIT")
        else:
            bpy.ops.object.mode_set(mode="OBJECT")
        return {'FINISHED'}

# Define Class Vertex
class ClassVertex(bpy.types.Operator):
    bl_idname = "class.vertex"
    bl_label = "Class Vertex"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        if bpy.ops.mesh.select_mode != "EDGE, FACE":
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            return {'FINISHED'}

# Define Class Edge
class ClassEdge(bpy.types.Operator):
    bl_idname = "class.edge"
    bl_label = "Class Edge"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        if bpy.ops.mesh.select_mode != "VERT, FACE":
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
            return {'FINISHED'}

# Define Class Face
class ClassFace(bpy.types.Operator):
    bl_idname = "class.face"
    bl_label = "Class Face"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        if bpy.ops.mesh.select_mode != "VERT, EDGE":
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            return {'FINISHED'}

######################
#   Selection Mode   #
######################

# Components Selection Mode
class VertsEdges(bpy.types.Operator):
    bl_idname = "verts.edges"
    bl_label = "Verts Edges"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.context.tool_settings.mesh_select_mode = (True, True, False)
        if bpy.context.object.mode == "EDIT":
            bpy.context.tool_settings.mesh_select_mode = (True, True, False)
            return {'FINISHED'}


class EdgesFaces(bpy.types.Operator):
    bl_idname = "edges.faces"
    bl_label = "EdgesFaces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.context.tool_settings.mesh_select_mode = (False, True, True)
        if bpy.context.object.mode == "EDIT":
            bpy.context.tool_settings.mesh_select_mode = (False, True, True)
            return {'FINISHED'}

class VertsFaces(bpy.types.Operator):
    bl_idname = "verts.faces"
    bl_label = "Verts Faces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.context.tool_settings.mesh_select_mode = (True, False, True)
        if bpy.context.object.mode == "EDIT":
            bpy.context.tool_settings.mesh_select_mode = (True, False, True)
            return {'FINISHED'}

class VertsEdgesFaces(bpy.types.Operator):
    bl_idname = "verts.edgesfaces"
    bl_label = "Verts Edges Faces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.context.tool_settings.mesh_select_mode = (True, True, True)
        if bpy.context.object.mode == "EDIT":
            bpy.context.tool_settings.mesh_select_mode = (True, True, True)
            return {'FINISHED'}

#Select All By Selection
class SelectAllBySelection(bpy.types.Operator):
    bl_idname = "object.selectallbyselection"
    bl_label = "Verts Edges Faces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        bpy.ops.mesh.select_all(action='TOGGLE')
        bpy.ops.mesh.select_all(action='TOGGLE')
        return {'FINISHED'}

######################
#       Views        #
######################

# Split area horizontal
class SplitHorizontal(bpy.types.Operator):
    bl_idname = "split.horizontal"
    bl_label = "split horizontal"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        bpy.ops.screen.area_split(direction='HORIZONTAL')
        return {'FINISHED'}

# Split area vertical
class SplitVertical(bpy.types.Operator):
    bl_idname = "split.vertical"
    bl_label = "split vertical"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        bpy.ops.screen.area_split(direction='VERTICAL')
        return {'FINISHED'}


# Join area
class JoinArea(bpy.types.Operator):
    """Join 2 area, clic on the second area to join"""
    bl_idname = "area.joinarea"
    bl_label = "Join Area"
    bl_options = {'REGISTER', 'UNDO'}

    min_x = IntProperty()
    min_y = IntProperty()

    def modal(self, context, event):
        if event.type == 'LEFTMOUSE':
            self.max_x = event.mouse_x
            self.max_y = event.mouse_y
            bpy.ops.screen.area_join(min_x=self.min_x, min_y=self.min_y, max_x=self.max_x, max_y=self.max_y)
            bpy.ops.screen.screen_full_area()
            bpy.ops.screen.screen_full_area()
            return {'FINISHED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        self.min_x = event.mouse_x
        self.min_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

#View Class menu
class ViewMenu(bpy.types.Operator):
    """Menu to change views"""
    bl_idname = "object.view_menu"
    bl_label = "View_Menu"
    bl_options = {'REGISTER', 'UNDO'}
    variable = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.context.area.type=self.variable
        return {'FINISHED'}
##############
#   Sculpt   #
##############

# Sculpt Polish
class SculptPolish(bpy.types.Operator):
    bl_idname = "sculpt.polish"
    bl_label = "Sculpt Polish"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        bpy.context.tool_settings.sculpt.brush=bpy.data.brushes['Polish']
        return {'FINISHED'}

# Sculpt Polish
class SculptSculptDraw(bpy.types.Operator):
    bl_idname = "sculpt.sculptraw"
    bl_label = "Sculpt SculptDraw"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        bpy.context.tool_settings.sculpt.brush=bpy.data.brushes['SculptDraw']
        return {'FINISHED'}

######################
#   Cursor/Origin    #
######################

#Pivot to selection
class PivotToSelection(bpy.types.Operator):
    bl_idname = "object.pivot2selection"
    bl_label = "Pivot To Selection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        saved_location = bpy.context.scene.cursor_location.copy()
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.scene.cursor_location = saved_location
        return {'FINISHED'}

#Pivot to Bottom
class PivotBottom(bpy.types.Operator):
    bl_idname = "object.pivotobottom"
    bl_label = "Pivot To Bottom"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        objlist = []
        for obj in bpy.context.selected_objects:
            objlist.append(obj)

        for obj in bpy.context.selected_objects:
            obj.select = False

        for obj in objlist:
            bpy.context.scene.objects.active = obj
            obj.select = True

            bpy.ops.view3d.snap_cursor_to_selected()
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bottom = 1000
            for v in obj.data.vertices:
                if v.co.z < bottom:
                    bottom = v.co.z
            bpy.context.space_data.cursor_location[2] = bottom
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            obj.select = False

        for obj in objlist:
            obj.select = True








#         bpy.ops.object.mode_set(mode = 'OBJECT')
#         bpy.ops.object.transform_apply(location=True, rotation=False, scale=True)
#         bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
#         o=bpy.context.active_object
#         init=0
#         for x in o.data.vertices:
#              if init==0:
#                  a=x.co.z
#                  init=1
#              elif x.co.z<a:
#                  a=x.co.z
#
#         for x in o.data.vertices:
#              x.co.z-=a
#
#         o.location.z+=a
#        bpy.ops.object.mode_set(mode = 'EDIT')
        return {'FINISHED'}

#####################
#   Simple Align    #
#####################
#Align X
class AlignX(bpy.types.Operator):
    bl_idname = "align.x"
    bl_label = "Align  X"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for vert in bpy.context.object.data.vertices:
            bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}

#Align Y
class AlignY(bpy.types.Operator):
    bl_idname = "align.y"
    bl_label = "Align  Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for vert in bpy.context.object.data.vertices:
            bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}

#Align Z
class AlignZ(bpy.types.Operator):
    bl_idname = "align.z"
    bl_label = "Align  Z"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for vert in bpy.context.object.data.vertices:
            bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}

#####################
#    Align To 0     #
#####################

#Align to X - 0
class AlignToX0(bpy.types.Operator):
    bl_idname = "align.2x0"
    bl_label = "Align To X-0"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.mode_set(mode = 'OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[0] = 0
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

#Align to Z - 0
class AlignToY0(bpy.types.Operator):
    bl_idname = "align.2y0"
    bl_label = "Align To Y-0"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.mode_set(mode = 'OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[1] = 0
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

#Align to Z - 0
class AlignToZ0(bpy.types.Operator):
    bl_idname = "align.2z0"
    bl_label = "Align To Z-0"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.mode_set(mode = 'OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[2] = 0
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

#Align X Left
class AlignXLeft(bpy.types.Operator):
    bl_idname = "alignx.left"
    bl_label = "Align X Left"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 0
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] < max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

#Align X Right
class AlignXRight(bpy.types.Operator):
    bl_idname = "alignx.right"
    bl_label = "Align X Right"

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 0
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] > max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

#Align Y Back
class AlignYBack(bpy.types.Operator):
    bl_idname = "aligny.back"
    bl_label = "Align Y back"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 1
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] > max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

#Align Y Front
class AlignYFront(bpy.types.Operator):
    bl_idname = "aligny.front"
    bl_label = "Align Y Front"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 1
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] < max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

#Align Z Top
class AlignZTop(bpy.types.Operator):
    bl_idname = "alignz.top"
    bl_label = "Align Z Top"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 2
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] > max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

#Align Z Bottom
class AlignZBottom(bpy.types.Operator):
    bl_idname = "alignz.bottom"
    bl_label = "Align Z Bottom"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 2
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] < max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

#################
#    Delete     #
#################

#Limited Dissolve
class DeleteLimitedDissolve(bpy.types.Operator):
    bl_idname = "delete.limiteddissolve"
    bl_label = "Delete Limited Dissolve"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        bpy.ops.mesh.dissolve_limited(angle_limit=3.14159, use_dissolve_boundaries=False)
        return {'FINISHED'}

####################
#    Animation     #
####################

#Insert Auto Keyframe
class InsertAutoKeyframe(bpy.types.Operator):
    bl_idname = "insert.autokeyframe"
    bl_label = "Insert Auto Keyframe"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if bpy.context.scene.tool_settings.use_keyframe_insert_auto == True :
            bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        if bpy.context.scene.tool_settings.use_keyframe_insert_auto == False :
            bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        return {'FINISHED'}

###########################
#    Apply Transforms     #
###########################

#Apply Transforms
class ApplyTransformLocation(bpy.types.Operator):
    bl_idname = "apply.transformlocation"
    bl_label = "Apply Transform Location"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
        return {'FINISHED'}

#Apply Transforms
class ApplyTransformRotation(bpy.types.Operator):
    bl_idname = "apply.transformrotation"
    bl_label = "Apply Transform Rotation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        return {'FINISHED'}

#Apply Transforms
class ApplyTransformScale(bpy.types.Operator):
    bl_idname = "apply.transformscale"
    bl_label = "Apply Transform Scale"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        return {'FINISHED'}

#Apply Transforms
class ApplyTransformRotationScale(bpy.types.Operator):
    bl_idname = "apply.transformrotationscale"
    bl_label = "Apply Transform Rotation Scale"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        return {'FINISHED'}

#Apply Transforms
class ApplyTransformAll(bpy.types.Operator):
    bl_idname = "apply.transformall"
    bl_label = "Apply Transform All"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        return {'FINISHED'}


# Clear Menu
class ClearMenu(bpy.types.Menu):
    bl_idname = "clear.menu"
    bl_label = "Clear Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.location_clear", text="Clear Location", icon='MAN_TRANS')
        layout.operator("object.rotation_clear", text="Clear Rotation", icon='MAN_ROT')
        layout.operator("object.scale_clear", text="Clear Scale", icon='MAN_SCALE')
        layout.operator("object.origin_clear", text="Clear Origin", icon='MANIPUL')

#Clear all
class ClearAll(bpy.types.Operator):
    bl_idname = "clear.all"
    bl_label = "Clear All"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.location_clear()
        bpy.ops.object.rotation_clear()
        bpy.ops.object.scale_clear()
        return {'FINISHED'}

########################
#    Open/Save/...     #
########################

#External Data
class ExternalData(bpy.types.Menu):
    bl_idname = "external.data"
    bl_label = "External Data"

    def draw(self, context):
        layout = self.layout

        layout.operator("file.autopack_toggle", text="Automatically Pack Into .blend")
        layout.separator()
        layout.operator("file.pack_all", text="Pack All Into .blend")
        layout.operator("file.unpack_all", text="Unpack All Into Files")
        layout.separator()
        layout.operator("file.make_paths_relative", text="Make All Paths Relative")
        layout.operator("file.make_paths_absolute", text="Make All Paths Absolute")
        layout.operator("file.report_missing_files", text="Report Missing Files")
        layout.operator("file.find_missing_files", text="Find Missing Files")

#Save Incremental
class FileIncrementalSave(bpy.types.Operator):
    bl_idname = "file.save_incremental"
    bl_label = "Save Incremental"
    bl_options = {"REGISTER"}

    def execute(self, context):
        f_path = bpy.data.filepath
        if f_path.find("_") != -1:
            str_nb = f_path.rpartition("_")[-1].rpartition(".blend")[0]
            int_nb = int(str_nb)
            new_nb = str_nb.replace(str(int_nb),str(int_nb+1))
            output = f_path.replace(str_nb,new_nb)

            i = 1
            while os.path.isfile(output):
                str_nb = f_path.rpartition("_")[-1].rpartition(".blend")[0]
                i += 1
                new_nb = str_nb.replace(str(int_nb),str(int_nb+i))
                output = f_path.replace(str_nb,new_nb)
        else:
            output = f_path.rpartition(".blend")[0]+"_001"+".blend"

        bpy.ops.wm.save_as_mainfile(filepath=output)
        self.report({'INFO'}, "File: {0} - Created at: {1}".format(output[len(bpy.path.abspath("//")):], output[:len(bpy.path.abspath("//"))]))
        return {'FINISHED'}

######################
#    Views Ortho     #
######################
#Persp/Ortho
class PerspOrthoView(bpy.types.Operator):
    bl_idname = "persp.orthoview"
    bl_label = "Persp/Ortho"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_persportho()
        return {'FINISHED'}
#######################################################
# Camera                                              #
#######################################################

#Lock Camera Transforms
class LockCameraTransforms(bpy.types.Operator):
    bl_idname = "object.lockcameratransforms"
    bl_label = "Lock Camera Transforms"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.lock_rotation[0] == False:
            bpy.context.object.lock_rotation[0] = True
            bpy.context.object.lock_rotation[1] = True
            bpy.context.object.lock_rotation[2] = True
            bpy.context.object.lock_location[0] = True
            bpy.context.object.lock_location[1] = True
            bpy.context.object.lock_location[2] = True
            bpy.context.object.lock_scale[0] = True
            bpy.context.object.lock_scale[1] = True
            bpy.context.object.lock_scale[2] = True

        elif bpy.context.object.lock_rotation[0] == True :
             bpy.context.object.lock_rotation[0] = False
             bpy.context.object.lock_rotation[1] = False
             bpy.context.object.lock_rotation[2] = False
             bpy.context.object.lock_location[0] = False
             bpy.context.object.lock_location[1] = False
             bpy.context.object.lock_location[2] = False
             bpy.context.object.lock_scale[0] = False
             bpy.context.object.lock_scale[1] = False
             bpy.context.object.lock_scale[2] = False
        return {'FINISHED'}

#Active Camera
bpy.types.Scene.cameratoto = bpy.props.StringProperty(default="")

class ActiveCameraSelection(bpy.types.Operator):
    bl_idname = "object.activecameraselection"
    bl_label = "Active Camera Selection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.data.objects[context.scene.cameratoto].select=True
        bpy.ops.view3d.object_as_camera()
        return {'FINISHED'}

#Select Camera
class CameraSelection(bpy.types.Operator):
    bl_idname = "object.cameraselection"
    bl_label = "Camera Selection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for cam in bpy.data.cameras:
            bpy.ops.object.select_camera()

        return {'FINISHED'}
######################
#     Pie Menus      #
######################

# Pie Edit/Object Others modes - Tab
class PieObjectEditotherModes(Menu):
    bl_idname = "pie.objecteditmodeothermodes"
    bl_label = "Select Other Modes"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("class.pieweightpaint", text="Weight Paint", icon='WPAINT_HLT')
        #6 - RIGHT
        pie.operator("class.pietexturepaint", text="Texture Paint", icon='TPAINT_HLT')
        #2 - BOTTOM
        pie.operator("class.pieparticleedit", text="Particle Edit", icon='PARTICLEMODE')
        #8 - TOP
        pie.operator("class.pievertexpaint", text="Vertex Paint", icon='VPAINT_HLT')
        #7 - TOP - LEFT
        #9 - TOP - RIGHT
        #1 - BOTTOM - LEFT
        #3 - BOTTOM - RIGHT

# Pie Vertex/Edges/Faces Modes - Tab
class PieVertexEdgesFacesModes(Menu):
    bl_idname = "pie.vertexedgesfacesmodes"
    bl_label = "Select Multi Components"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("verts.faces", text="Vertex/Faces", icon='LOOPSEL')
        #6 - RIGHT
        pie.operator("verts.edges", text="Vertex/Edges", icon='VERTEXSEL')
        #2 - BOTTOM
        pie.operator("verts.edgesfaces", text="Vertex/Edges/Faces", icon='OBJECT_DATAMODE')
        #8 - TOP
        pie.operator("edges.faces", text="Edges/Faces", icon='FACESEL')
        #7 - TOP - LEFT
        #9 - TOP - RIGHT
        #1 - BOTTOM - LEFT
        #3 - BOTTOM - RIGHT


  #ミドルマウス MIDDLE
# Pie Select Mode - Tab
class PieObjectEditMode(Menu):
    bl_idname = "pie.objecteditmode"
    bl_label = "Select Mode"

    def draw(self, context):
        layout = self.layout

        ob = context
        if ob.object.type == 'MESH':
            pie = layout.menu_pie()
            #4 - LEFT
            pie.operator("class.vertex", text="Vertex", icon='VERTEXSEL')
            #6 - RIGHT
            pie.operator("screen.redo_last", text="Setting", icon='SETTINGS')
            #2 - BOTTOM
            pie.operator("class.face", text="Face", icon='FACESEL')
            #8 - TOP
            pie.operator("class.edge", text="Edge", icon='EDGESEL')
            #7 - TOP - LEFT
            pie.operator("wm.context_toggle", text="Limit to Visible", icon="ORTHO").data_path = "space_data.use_occlude_geometry"
            #9 - TOP - RIGHT
            pie.operator("class.object", text="Edit/Object", icon='OBJECT_DATAMODE')
            #Multi Object UV Editing
            if bpy.context.object.mode == "OBJECT":
                pie.operator("object.multi_object_uv_edit", text="Multi UV", icon='IMAGE_RGB')





                #pie.operator("sculpt.sculptmode_toggle", text="Sculpt", icon='SCULPTMODE_HLT')
            #1 - BOTTOM - LEFT
#            pie.operator("wm.call_menu_pie", text="Other Modes", icon='TPAINT_HLT').name="pie.objecteditmodeothermodes"
            #3 - BOTTOM - RIGHT
#            pie.operator("wm.call_menu_pie", text="V/E/F Modes", icon='UV_VERTEXSEL').name="pie.vertexedgesfacesmodes"

        elif ob.object.type == 'CURVE':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

        elif ob.object.type == 'ARMATURE':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit Mode", icon='OBJECT_DATAMODE')
            pie.operator("object.posemode_toggle", text="Pose", icon='POSE_HLT')
            pie.operator("class.object", text="Object Mode", icon='OBJECT_DATAMODE')

        elif ob.object.type == 'FONT':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

        elif ob.object.type == 'SURFACE':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

        elif ob.object.type == 'ARMATURE':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

        elif ob.object.type == 'META':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

        elif ob.object.type == 'LATTICE':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

        elif ob.object.type == 'ARMATURE':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

#Pie View Animation Etc - Space
class PieAnimationEtc(Menu):
    bl_idname = "pie.animationetc"
    bl_label = "Animation Etc"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("object.view_menu", text="Timeline", icon= 'TIME').variable="TIMELINE"
        #6 - RIGHT
        pie.operator("object.view_menu", text="Dope Sheet", icon= 'ACTION').variable="DOPESHEET_EDITOR"
        #2 - BOTTOM
        pie.operator("object.view_menu", text="NLA Editor", icon= 'NLA').variable="NLA_EDITOR"
        #8 - TOP
        pie.operator("object.view_menu", text="Graph Editor", icon= 'IPO').variable="GRAPH_EDITOR"
        #7 - TOP - LEFT
        pie.operator("object.view_menu", text="Movie Clip Editor", icon= 'RENDER_ANIMATION').variable="CLIP_EDITOR"
        #9 - TOP - RIGHT
        pie.operator("object.view_menu", text="Sequence Editor", icon= 'SEQUENCE').variable="SEQUENCE_EDITOR"
        #1 - BOTTOM - LEFT
        pie.operator("object.view_menu", text="Logic Editor", icon= 'LOGIC').variable="LOGIC_EDITOR"
        #3 - BOTTOM - RIGHT

#Pie View File Properties Etc - Space
class PieFilePropertiesEtc(Menu):
    bl_idname = "pie.filepropertiesetc"
    bl_label = "Pie File Properties..."

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("object.view_menu", text="Properties", icon= 'BUTS').variable="PROPERTIES"
        #6 - RIGHT
        pie.operator("object.view_menu", text="Outliner", icon= 'OOPS').variable="OUTLINER"
        #2 - BOTTOM
        pie.operator("object.view_menu", text="User Preferences", icon= 'PREFERENCES').variable="USER_PREFERENCES"
        #8 - TOP
        pie.operator("object.view_menu", text="Text Editor", icon= 'FILE_TEXT').variable="TEXT_EDITOR"
        #7 - TOP - LEFT
        pie.operator("object.view_menu", text="File Browser", icon= 'FILESEL').variable="FILE_BROWSER"
        #1 - BOTTOM - LEFT
        pie.operator("object.view_menu", text="Python Console", icon= 'CONSOLE').variable="CONSOLE"
        #9 - TOP - RIGHT
        pie.operator("object.view_menu", text="Info", icon= 'INFO').variable="INFO"
        #3 - BOTTOM - RIGHT

#Pie View All Sel Glob Etc - Q
class PieViewallSelGlobEtc(Menu):
    bl_idname = "pie.vieallselglobetc"
    bl_label = "Pie View All Sel Glob..."

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("view3d.view_all", text="View All").center = True
        #6 - RIGHT
        pie.operator("view3d.view_selected", text="View Selected")
        #2 - BOTTOM
        pie.operator("persp.orthoview", text="Persp/Ortho", icon='RESTRICT_VIEW_OFF')
        #8 - TOP
        pie.operator("view3d.localview", text="Local/Global")
        #7 - TOP - LEFT
        pie.operator("screen.region_quadview", text="Toggle Quad View", icon='SPLITSCREEN')
        #1 - BOTTOM - LEFT
        pie.operator("screen.screen_full_area", text="Full Screen", icon='FULLSCREEN_ENTER')
        #9 - TOP - RIGHT
        #3 - BOTTOM - RIGHT

#Pie Views - Space
class PieAreaViews(Menu):
    bl_idname = "pie.areaviews"
    bl_label = "Pie Views"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("object.view_menu", text="Image Editor", icon= 'IMAGE_COL').variable="IMAGE_EDITOR"

        #6 - RIGHT
        pie.operator("object.view_menu", text="Text Editor", icon= 'FILE_TEXT').variable="TEXT_EDITOR"
        #2 - BOTTOM
        pie.operator("object.view_menu", text="Node Editor", icon= 'NODETREE').variable="NODE_EDITOR"

        #pie.operator_context="INVOKE_DEFAULT"
        #pie.operator("area.joinarea", icon='X', text="Join Area")
        #8 - TOP
        pie.operator("object.view_menu", text="VIEW 3D", icon= 'VIEW3D').variable="VIEW_3D"
        #7 - TOP - LEFT

        pie.operator("object.view_menu", text="User Preferences", icon= 'PREFERENCES').variable="USER_PREFERENCES"
        #9 - TOP - RIGHT
        pie.operator("object.view_menu", text="Properties", icon= 'BUTS').variable="PROPERTIES"
#
#         #ファイル、プロパティ関連
#         box = pie.split().column()
#         row = box.row(align=True)
#         box.operator("object.view_menu", text="Properties", icon= 'BUTS').variable="PROPERTIES"
#         box.operator("object.view_menu", text="Outliner", icon= 'OOPS').variable="OUTLINER"
#         box.operator("object.view_menu", text="User Preferences", icon= 'PREFERENCES').variable="USER_PREFERENCES"
#         box.operator("object.view_menu", text="Python Console", icon= 'CONSOLE').variable="CONSOLE"
#
#
#
#
#
# #アニメーション関連
#
#
#         box = pie.split().column()
#         row = box.row(align=True)
#         box.operator("object.view_menu", text="Timeline", icon= 'TIME').variable="TIMELINE"
#         box.operator("object.view_menu", text="NLA Editor", icon= 'NLA').variable="NLA_EDITOR"
#         box.operator("object.view_menu", text="Movie Clip Editor", icon= 'RENDER_ANIMATION').variable="CLIP_EDITOR"
#         box.operator("object.view_menu", text="Sequence Editor", icon= 'SEQUENCE').variable="SEQUENCE_EDITOR"
#


        #1 - BOTTOM - LEFT
        pie.operator("object.view_menu", text="Dope Sheet", icon= 'ACTION').variable="DOPESHEET_EDITOR"
        #3 - BOTTOM - RIGHT
        pie.operator("object.view_menu", text="Graph Editor", icon= 'IPO').variable="GRAPH_EDITOR"

#Pie Camera - C
class PieCamera(Menu):
    bl_idname = "pie.camera"
    bl_label = "Pie Camera"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        ob = bpy.context.object
        obj = context.object

        #4 - LEFT
        if context.space_data.lock_camera == False:
            pie.operator("wm.context_toggle", text="Lock Cam to View", icon='UNLOCKED').data_path = "space_data.lock_camera"
        elif context.space_data.lock_camera == True:
            pie.operator("wm.context_toggle", text="Lock Cam to View", icon='LOCKED').data_path = "space_data.lock_camera"
        #6 - RIGHT
        pie.operator("view3d.viewnumpad", text="View Camera", icon='VISIBLE_IPO_ON').type='CAMERA'
        #2 - BOTTOM
        pie.operator("view3d.camera_to_view", text="Cam to view", icon = 'MAN_TRANS')
        #8 - TOP
        if ob.lock_rotation[0] == False:
            pie.operator("object.lockcameratransforms", text="Lock Transforms", icon = 'UNLOCKED')
        elif  ob.lock_rotation[0] == True:
            pie.operator("object.lockcameratransforms", text="Lock Transforms", icon = 'LOCKED')
        #7 - TOP - LEFT
        #9 - TOP - RIGHT
        #1 - BOTTOM - LEFT
        #3 - BOTTOM - RIGHT

#Pie views numpad - Q
class PieViewNumpad(Menu):
    bl_idname = "pie.viewnumpad"
    bl_label = "Pie Views Ortho"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("view3d.viewnumpad", text="Left", icon='TRIA_LEFT').type='LEFT'
        #6 - RIGHT
        pie.operator("view3d.viewnumpad", text="Right", icon='TRIA_RIGHT').type='RIGHT'
        #2 - BOTTOM
        pie.operator("view3d.viewnumpad", text="Bottom", icon='TRIA_DOWN').type='BOTTOM'
        #8 - TOP
        pie.operator("view3d.viewnumpad", text="Top", icon='TRIA_UP').type='TOP'
        #7 - TOP - LEFT
        pie.operator("view3d.viewnumpad", text="Front").type='FRONT'
        #9 - TOP - RIGHT
        pie.operator("view3d.viewnumpad", text="Back").type='BACK'
        #1 - BOTTOM - LEFT
        pie.operator("wm.call_menu_pie", text="Camera", icon='CAMERA_DATA').name="pie.camera"

        #3 - BOTTOM - RIGHT
        pie.operator("wm.call_menu_pie", text="View All/Sel/Glob...", icon='BBOX').name="pie.vieallselglobetc"

#Pie Sculp Pie Menus - W
class PieSculptPie(Menu):
    bl_idname = "pie.sculpt"
    bl_label = "Pie Sculpt"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("paint.brush_select", text="Crease", icon='BRUSH_CREASE').sculpt_tool='CREASE'
        #6 - RIGHT
        pie.operator("paint.brush_select", text="Clay", icon='BRUSH_CLAY').sculpt_tool='CLAY'
        #2 - BOTTOM
        pie.operator("paint.brush_select", text='Flatten', icon='BRUSH_FLATTEN').sculpt_tool='FLATTEN'
        #8 - TOP
        pie.operator("paint.brush_select", text='Brush', icon='BRUSH_SCULPT_DRAW').sculpt_tool='DRAW'
        #7 - TOP - LEFT
        pie.operator("paint.brush_select", text='Inflate/Deflate', icon='BRUSH_INFLATE').sculpt_tool='INFLATE'
        #9 - TOP - RIGHT
        pie.operator("paint.brush_select", text='Grab', icon='BRUSH_GRAB').sculpt_tool='GRAB'
        #1 - BOTTOM - LEFT
        pie.operator("paint.brush_select", text='Mask', icon='BRUSH_MASK').sculpt_tool='MASK'
        #3 - BOTTOM - RIGHT
        pie.operator("wm.call_menu_pie", text="Others Brushes", icon='LINE_DATA').name="pie.sculpttwo"

#Pie Sculp Pie Menus 2 - W
class PieSculpttwo(Menu):
    bl_idname = "pie.sculpttwo"
    bl_label = "Pie Sculpt 2"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("paint.brush_select", text='Claystrips', icon='BRUSH_CREASE').sculpt_tool= 'CLAY_STRIPS'
        #6 - RIGHT
        pie.operator("paint.brush_select", text='Blob', icon='BRUSH_BLOB').sculpt_tool= 'BLOB'
        #2 - BOTTOM
        pie.operator("paint.brush_select", text='Snakehook', icon='BRUSH_SNAKE_HOOK').sculpt_tool= 'SNAKE_HOOK'
        #8 - TOP
        pie.operator("paint.brush_select", text='Smooth', icon='BRUSH_SMOOTH').sculpt_tool= 'SMOOTH'
        #7 - TOP - LEFT
        pie.operator("paint.brush_select", text='Pinch/Magnify', icon='BRUSH_PINCH').sculpt_tool= 'PINCH'
        #9 - TOP - RIGHT
        pie.operator("sculpt.polish", text='Polish', icon='BRUSH_FLATTEN')
        #1 - BOTTOM - LEFT
        box = pie.split().column()
        row = box.row(align=True)
        box.operator("paint.brush_select", text='Twist', icon='BRUSH_ROTATE').sculpt_tool= 'ROTATE'
        box.operator("paint.brush_select", text='Scrape/Peaks', icon='BRUSH_SCRAPE').sculpt_tool= 'SCRAPE'
        box.operator("sculpt.sculptraw", text='SculptDraw', icon='BRUSH_SCULPT_DRAW')
        #3 - BOTTOM - RIGHT
        box = pie.split().column()
        row = box.row(align=True)
        box.operator("paint.brush_select", text='Layer', icon='BRUSH_LAYER').sculpt_tool= 'LAYER'
        box.operator("paint.brush_select", text='Nudge', icon='BRUSH_NUDGE').sculpt_tool= 'NUDGE'
        box.operator("paint.brush_select", text='Thumb', icon='BRUSH_THUMB').sculpt_tool= 'THUMB'
        box.operator("paint.brush_select", text='Fill/Deepen', icon='BRUSH_FILL').sculpt_tool='FILL'






#Pie Origin/Pivot - Shift + S
class PieOriginPivot(Menu):
    bl_idname = "pie.originpivot"
    bl_label = "Pie Origin/Cursor"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("object.pivotobottom", text="Origin to Bottom", icon='TRIA_DOWN')
        #6 - RIGHT
        pie.operator("view3d.snap_cursor_to_selected", text="Cursor to Selected", icon='ROTACTIVE')
        #2 - BOTTOM
        pie.operator("view3d.snap_selected_to_cursor", text="Selection to Cursor", icon='CLIPUV_HLT').use_offset = False
        #8 - TOP 編集xx
        pie.operator("object.origin_set_cursor_x", text="Origin To 3D Cursor", icon='CURSOR')
        # pie.operator("object.origin_set", text="Origin To 3D Cursor", icon='CURSOR').type ='ORIGIN_CURSOR'
        #7 - TOP - LEFT
#        pie.operator("object.pivot2selection", text="Origin To Selection", icon='SNAP_INCREMENT')
        pie.operator("object.ralign_orientation_to_selection", text="Restore Rotate", icon='LAMP_AREA') #編集
        #9 - TOP - RIGHT
        pie.operator("object.origin_set", text="Origin To Geometry", icon='ROTATE').type ='ORIGIN_GEOMETRY'
        #1 - BOTTOM - LEFT
        pie.operator("object.origin_set", text="Geometry To Origin", icon='BBOX').type ='GEOMETRY_ORIGIN'
        #3 - BOTTOM - RIGHT
        pie.operator("wm.call_menu_pie", text="Others", icon='CURSOR').name="origin.pivotmenu"

#Pie Pivot Point - Shit + S
class PiePivotPoint(Menu):
    bl_idname = "pie.pivotpoint"
    bl_label = "Pie Pivot Point"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("pivotpoint.variable", text="Active Element", icon='ROTACTIVE').variable = 'ACTIVE_ELEMENT'
        #6 - RIGHT
        pie.operator("pivotpoint.variable", text="Median Point", icon='ROTATECENTER').variable = 'MEDIAN_POINT'
        #2 - BOTTOM
        pie.operator("pivotpoint.variable", text="Individual Origins", icon='ROTATECOLLECTION').variable = 'INDIVIDUAL_ORIGINS'
        #8 - TOP
        pie.operator("pivotpoint.variable", text="Cursor", icon='CURSOR').variable = 'CURSOR'
        #7 - TOP - LEFT
        pie.operator("pivotpoint.variable", text="Bounding Box Center", icon='ROTATE').variable = 'BOUNDING_BOX_CENTER'
        #9 - TOP - RIGHT
        pie.operator("use.pivotalign", text="Use Pivot Align", icon='ALIGN')
        #1 - BOTTOM - LEFT
        #3 - BOTTOM - RIGHT

#Origin/Pivot menu1  - Shift + S
class OriginPivotMenu(Menu):
    bl_idname = "origin.pivotmenu"
    bl_label = "Origin Pivot Menu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("view3d.snap_selected_to_cursor", text="Selection to Cursor (Offset)", icon='CURSOR').use_offset = True
        #6 - RIGHT
        pie.operator("view3d.snap_selected_to_grid", text="Selection to Grid", icon='GRID')
        #2 - BOTTOM
        pie.operator("object.origin_set", text="Origin to Center of Mass", icon='BBOX').type = 'ORIGIN_CENTER_OF_MASS'
        #8 - TOP
        pie.operator("view3d.snap_cursor_to_center", text="Cursor to Center", icon='CLIPUV_DEHLT')
        #7 - TOP - LEFT
        pie.operator("view3d.snap_cursor_to_grid", text="Cursor to Grid", icon='GRID')
        #9 - TOP - RIGHT
        pie.operator("view3d.snap_cursor_to_active", text="Cursor to Active", icon='BBOX')
        #1 - BOTTOM - LEFT
        #3 - BOTTOM - RIGHT

#Pie Manipulators - Ctrl + Space
class PieManipulator(Menu):
    bl_idname = "pie.manipulator"
    bl_label = "Pie Manipulator"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("manip.translate", text="Translate", icon='MAN_TRANS')
        #6 - RIGHT
        pie.operator("manip.scale", text="scale", icon='MAN_SCALE')
        #2 - BOTTOM
        pie.operator("manip.rotate", text="Rotate", icon='MAN_ROT')
        #8 - TOP
        pie.operator("w.manupulators", text="Manipulator", icon='MANIPUL')
        #7 - TOP - LEFT
        pie.operator("translate.rotate", text="Translate/Rotate")
        #9 - TOP - RIGHT
        pie.operator("translate.scale", text="Translate/Scale")
        #1 - BOTTOM - LEFT
        pie.operator("rotate.scale", text="Rotate/Scale")
        #3 - BOTTOM - RIGHT
        pie.operator("translate.rotatescale", text="Translate/Rotate/Scale")

#Pie Snapping - Shift + Tab
class PieSnaping(Menu):
    bl_idname = "pie.snapping"
    bl_label = "Pie Snapping"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("snap.vertex", text="Vertex", icon='SNAP_VERTEX')
        #6 - RIGHT
        pie.operator("snap.face", text="Face", icon='SNAP_FACE')
        #2 - BOTTOM
        pie.operator("snap.edge", text="Edge", icon='SNAP_EDGE')
        #8 - TOP
        pie.prop(context.tool_settings, "use_snap", text="Snap On/Off")
        #7 - TOP - LEFT
        pie.operator("snap.volume", text="Volume", icon='SNAP_VOLUME')
        #9 - TOP - RIGHT
        pie.operator("snap.increment", text="Increment", icon='SNAP_INCREMENT')
        #1 - BOTTOM - LEFT
        pie.operator("snap.alignrotation", text="Align rotation", icon='SNAP_NORMAL')
        #3 - BOTTOM - RIGHT
        pie.operator("wm.call_menu_pie", text="Snap Target", icon='SNAP_SURFACE').name="snap.targetmenu"

#Menu Snap Target - Shift + Tab
class SnapTargetMenu(Menu):
    bl_idname = "snap.targetmenu"
    bl_label = "Snap Target Menu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("object.snaptargetvariable", text="Active").variable='ACTIVE'
        #6 - RIGHT
        pie.operator("object.snaptargetvariable", text="Median").variable='MEDIAN'
        #2 - BOTTOM
        pie.operator("object.snaptargetvariable", text="Center").variable='CENTER'
        #8 - TOP
        pie.operator("object.snaptargetvariable", text="Closest").variable='CLOSEST'
        #7 - TOP - LEFT
        #9 - TOP - RIGHT
        #1 - BOTTOM - LEFT
        #3 - BOTTOM - RIGHT




##===============================================================

## Define Class Particle Edit
#class UserOrientation(bpy.types.Operator):
#    bl_idname = "object.xxx"
#    bl_options = {'REGISTER', 'UNDO'}
#
#
#    def execute(self, context):
#        bpy.ops.transform.create_orientation()
#        bpy.ops.object.orientationvariable(variable = 'Edge')
#
#        return {'FINISHED'}

##===============================================================





#Pie Orientation - Alt + Space
class PieOrientation(Menu):
    bl_idname = "pie.orientation"
    bl_label = "Pie Orientation"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("object.orientationvariable", text="View").variable = 'VIEW'
        #6 - RIGHT
        pie.operator("object.orientationvariable", text="Local").variable = 'LOCAL'
        #2 - BOTTOM
        pie.operator("object.orientationvariable", text="Normal").variable = 'NORMAL'
        #8 - TOP
        pie.operator("object.orientationvariable", text="Global").variable = 'GLOBAL'
        #7 - TOP - LEFT
        pie.operator("object.orientationvariable", text="Gimbal").variable = 'GIMBAL'
        #9 - TOP - RIGHT
        pie.operator("object.orientationvariable", text="EDGE").variable = 'Edge'
        #1 - BOTTOM - LEFT
#        pie.operator("transform.create_orientation", text="Add", icon='ZOOMIN')
        pie.operator("object.xxx2", text="Add", icon='ZOOMIN')
          #3 - BOTTOM - RIGHT
        pie.operator("transform.delete_orientation", text="Del", icon='X')

#Pie Shading - Z
class PieShadingView(Menu):
    bl_idname = "pie.shadingview"
    bl_label = "Pie Shading"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("object.shadingvariable", text="Material", icon='MATERIAL').variable = 'MATERIAL'
        #6 - RIGHT
        pie.operator("object.shadingvariable", text="Wireframe", icon='WIRE').variable = 'WIREFRAME'
        #2 - BOTTOM
#        pie.operator("object.shadingvariable", text="Texture", icon='TEXTURE_SHADED').variable = 'TEXTURED'
        pie.operator("object.wireall", text="Wire all", icon='COLOR_GREEN')
        #8 - TOP
        pie.operator("object.shadingvariable", text="Solid", icon='SOLID').variable = 'SOLID'
        #7 - TOP - LEFT
        pie.operator("wm.context_toggle", text="Hidden Wire", icon='GHOST_ENABLED').data_path = "space_data.show_occlude_wire"
        #pie.operator("object.shadingvariable", text="Bounding box", icon='BBOX').variable = 'BOUNDBOX'
        #9 - TOP - RIGHT
        pie.operator("object.shadingvariable", text="Render", icon='SMOOTH').variable = 'RENDERED'
        #1 - BOTTOM - LEFT
        pie.operator("shading.smooth", text="Shade Smooth", icon='SOLID')
        #3 - BOTTOM - RIGHT
        pie.operator("shading.flat", text="Shade Flat", icon='MESH_ICOSPHERE')

#Pie Object Shading 2 - Shift + Z
class PieObjectShading2(Menu):
    bl_idname = "pie.objectshading2"
    bl_label = "Pie Shading Object Others"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("wm.context_toggle", text="Only Render", icon='SOLID').data_path = "space_data.show_only_render"
        #6 - RIGHT
        pie.operator("scene.togglegridaxis", text="Show/Hide Grid", icon="MESH_GRID")
        #2 - BOTTOM
        pie.menu("meshdisplay.overlays", text="Mesh display")
        #8 - TOP
        pie.menu("normals.menu", text="Normals", icon='FACESEL')
        #7 - TOP - LEFT
        pie.menu("auto.smooth_menu", text="Auto Smooth", icon='MESH_DATA')
        #9 - TOP - RIGHT
        pie.operator("wm.context_toggle", text="Matcaps", icon='MATCAP_02').data_path = "space_data.use_matcap"
        #1 - BOTTOM - LEFT

        #3 - BOTTOM - RIGHT

#Pie Object Shading- Shift + Z
class PieObjectShading(Menu):
    bl_idname = "pie.objectshading"
    bl_label = "Pie Shading Object"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("wm.context_toggle", text="Backface Culling", icon="ORTHO").data_path = "space_data.show_backface_culling"
        #6 - RIGHT
        pie.operator("wire.selectedall", text="Wire", icon='WIRE')
        #2 - BOTTOM
        pie.operator("wm.context_toggle", text="Auto Merge", icon='AUTOMERGE_ON').data_path = "scene.tool_settings.use_mesh_automerge"
        #8 - TOP
        pie.operator("wm.context_toggle", text="Xray", icon='META_CUBE').data_path = "object.show_x_ray"
        #7 - TOP - LEFT
        pie.operator("wm.context_toggle", text="Show Normals Faces", icon='FACESEL').data_path = "object.data.show_normal_face"
        #9 - TOP - RIGHT
        pie.operator("wm.context_toggle", text="Hidden Wire", icon='GHOST_ENABLED').data_path = "space_data.show_occlude_wire"
        #1 - BOTTOM - LEFT


        pie.operator("wm.context_toggle", text="Double sided", icon='SNAP_FACE').data_path = "object.data.show_double_sided"
        #3 - BOTTOM - RIGHT
        pie.operator("wm.call_menu_pie", text="Others", icon='GROUP').name="pie.objectshading2"

#Pie ProportionalEditObj - O
class PieProportionalObj(Menu):
    bl_idname = "pie.proportional_obj"
    bl_label = "Pie Proportional Edit Obj"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("proportional_obj.sphere", text="Sphere", icon='SPHERECURVE')
        #6 - RIGHT
        pie.operator("proportional_obj.root", text="Root", icon='ROOTCURVE')
        #2 - BOTTOM
        pie.operator("proportional_obj.smooth", text="Smooth", icon='SMOOTHCURVE')
        #8 - TOP
        pie.prop(context.tool_settings, "use_proportional_edit_objects", text="Proportional On/Off")
        #7 - TOP - LEFT
        pie.operator("proportional_obj.linear", text="Linear", icon='LINCURVE')
        #9 - TOP - RIGHT
        pie.operator("proportional_obj.sharp", text="Sharp", icon='SHARPCURVE')
        #1 - BOTTOM - LEFT
        pie.operator("proportional_obj.constant", text="Constant", icon='NOCURVE')
        #3 - BOTTOM - RIGHT
        pie.operator("proportional_obj.random", text="Random", icon='RNDCURVE')

#Pie ProportionalEditEdt - O
class PieProportionalEdt(Menu):
    bl_idname = "pie.proportional_edt"
    bl_label = "Pie Proportional Edit"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("proportional_edt.connected", text="Connected", icon='PROP_CON')
        #6 - RIGHT
        pie.operator("proportional_edt.projected", text="Projected", icon='PROP_ON')
        #2 - BOTTOM
        pie.operator("proportional_edt.smooth", text="Smooth", icon='SMOOTHCURVE')
        #8 - TOP
        pie.operator("proportional_edt.active", text="Proportional On/Off", icon='PROP_ON')
        #7 - TOP - LEFT
        pie.operator("proportional_edt.sphere", text="Sphere", icon='SPHERECURVE')
        #9 - TOP - RIGHT
        pie.operator("proportional_edt.root", text="Root", icon='ROOTCURVE')
        #1 - BOTTOM - LEFT
        pie.operator("proportional_edt.constant", text="Constant", icon='NOCURVE')
        #3 - BOTTOM - RIGHT
        box = pie.split().column()
        row = box.row(align=True)
        box.operator("proportional_edt.linear", text="Linear", icon='LINCURVE')
        box.operator("proportional_edt.sharp", text="Sharp", icon='SHARPCURVE')
        box.operator("proportional_edt.random", text="Random", icon='RNDCURVE')

# Pie Align - Alt + X
class PieAlign(Menu):
    bl_idname = "pie.align"
    bl_label = "Pie Align"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("align.x", text="Align X", icon='TRIA_LEFT')
        #6 - RIGHT
        pie.operator("align.z", text="Align Z", icon='TRIA_DOWN')
        #2 - BOTTOM
        pie.operator("align.y", text="Align Y", icon='PLUS')
        #8 - TOP
        pie.operator("align.2y0", text="Align To Y-0")
        #7 - TOP - LEFT
        pie.operator("align.2x0", text="Align To X-0")
        #9 - TOP - RIGHT
        pie.operator("align.2z0", text="Align To Z-0")
        #1 - BOTTOM - LEFT
        #pie.menu("align.xyz")
        box = pie.split().box().column()
        box.label("Align :")
        row = box.row(align=True)
        row.label("X")
        row.operator("alignx.left", text="Neg")
        row.operator("alignx.right", text="Pos")
        row = box.row(align=True)
        row.label("Y")
        row.operator("aligny.front", text="Neg")
        row.operator("aligny.back", text="Pos")
        row = box.row(align=True)
        row.label("Z")
        row.operator("alignz.bottom", text="Neg")
        row.operator("alignz.top", text="Pos")
        #3 - BOTTOM - RIGHT
        box = pie.split().column()
        row = box.row(align=True)
        box.operator("mesh.vertex_align", icon='ALIGN', text="Align")
        box.operator("retopo.space", icon='ALIGN', text="Distribute")
        box.operator("mesh.vertex_inline", icon='ALIGN', text="Align & Distribute")

# Pie Delete - X
class PieDelete(Menu):
    bl_idname = "pie.delete"
    bl_label = "Pie Delete"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
       # pie.operator("mesh.delete", text="Delete Vertices", icon='VERTEXSEL').type='VERT'
        #6 - RIGHT
        #pie.operator("mesh.delete", text="Delete Faces", icon='FACESEL').type='FACE'
        #2 - BOTTOM
        #pie.operator("mesh.delete", text="Delete Edges", icon='EDGESEL').type='EDGE'
         #7 - TOP - LEFT
        pie.operator("mesh.dissolve_verts", text="Dissolve Vertices", icon='SNAP_VERTEX')
        #8 - TOP
        pie.operator("mesh.dissolve_edges", text="Dissolve Edges", icon='SNAP_EDGE')

        #9 - TOP - RIGHT
        pie.operator("mesh.dissolve_faces", text="Dissolve Faces", icon='SNAP_FACE')
        #1 - BOTTOM - LEFT
        box = pie.split().column()
        row = box.row(align=True)
        box.operator("delete.limiteddissolve", text="Limited Dissolve", icon= 'STICKY_UVS_LOC')
        box.operator("mesh.delete_edgeloop", text="Delete Edge Loops", icon='BORDER_LASSO')
        box.operator("mesh.edge_collapse", text="Edge Collapse", icon='UV_EDGESEL')
        #3 - BOTTOM - RIGHT
        box = pie.split().column()
        row = box.row(align=True)
        box.operator("mesh.delete", text="Only Edge & Faces", icon='SPACE2').type='EDGE_FACE'
        box.operator("mesh.delete", text="Only Faces", icon='UV_FACESEL').type='ONLY_FACE'

# Pie Apply Transforms - Ctrl + A
class PieApplyTransforms(Menu):
    bl_idname = "pie.applytranforms"
    bl_label = "Pie Apply Transforms"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("apply.transformlocation", text="Location", icon='MAN_TRANS')
        #6 - RIGHT
        pie.operator("apply.transformscale", text="Scale", icon='MAN_SCALE')
        #2 - BOTTOM
        pie.operator("apply.transformrotation", text="Rotation", icon='MAN_ROT')
        #8 - TOP
        pie.operator("apply.transformall", text="Transforms", icon='FREEZE')
        #7 - TOP - LEFT
        pie.operator("apply.transformrotationscale", text="Rotation/Scale")
        #9 - TOP - RIGHT
        pie.operator("clear.all", text="Clear All", icon='MANIPUL')
        #1 - BOTTOM - LEFT
        box = pie.split().column()
        row = box.row(align=True)
        box.operator("object.visual_transform_apply", text="Visual Transforms")
        box.operator("object.duplicates_make_real", text="Make Duplicates Real")
        #3 - BOTTOM - RIGHT
        pie.menu("clear.menu", text="Clear Transforms")

# Pie Selection Object Mode - A
class PieSelectionsOM(Menu):
    bl_idname = "pie.selectionsom"
    bl_label = "Pie Selections Object Mode"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("object.select_camera", text="Select Camera", icon='CAMERA_DATA')
        pie.operator("object.select_linked", text="Link dep", icon='CONSTRAINT_BONE').type='OBDATA'
        pie.operator("object.select_grouped", text="Layer", icon='LAYER_ACTIVE').type='LAYER'
        #3 - BOTTOM - RIGHT
        pie.operator("object.select_by_type", text="Select By Type", icon='SNAP_VOLUME')
        pie.operator("object.select_grouped", text="Select Grouped", icon='ROTATE')
        pie.operator("object.select_linked", text="Select Linked", icon='CONSTRAINT_BONE')
        pie.operator("object.select_grouped", text="Children", icon='FORCE_LENNARDJONES').type='CHILDREN_RECURSIVE'
        pie.operator("object.select_grouped", text=" Parent", icon='FORCE_FORCE').type='PARENT'



# Pie Selection Edit Mode
class PieSelectionsEM(Menu):
    bl_idname = "pie.selectionsem"
    bl_label = "Pie Selections Edit Mode"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        # pie.operator("mesh.select_all", text="Invert Selection", icon='FILE_REFRESH').action='INVERT'
        pie.operator("mesh.loop_multi_select", icon='PARTICLE_PATH', text="Edge Loops").ring=False #辺ループ
        #6 - RIGHT
        pie.operator("mesh.select_similar", text="Select Similar", icon='GHOST')
        #2 - BOTTOM
        pie.operator("mesh.select_nth", icon='PARTICLE_POINT') #チェッカーセレクト
#        pie.operator("view3d.select_border", text="Border Select", icon='BORDER_RECT')
        #8 - TOP
        pie.operator("mesh.loop_to_region", icon='BORDER_RECT')
         #7 - TOP - LEFT
        pie.operator("mesh.loop_multi_select", icon='UV_EDGESEL').ring=True
        #9 - TOP - RIGHT
        # pie.operator("wm.call_menu", name="edit_mesh_faces")
        #1 - BOTTOM - LEFT
        pie.operator("mesh.region_to_loop", icon='PARTICLE_POINT') #チェッカーセレクト
        pie.operator("mesh.select_more", icon='ZOOMIN')
        pie.operator("mesh.select_less", icon='ZOOMOUT')

       # box = pie.split().column()
     #   row = box.row(align=True)

   #     box.operator("mesh.select_similar", text="PERIMETER").type='PERIMETER' #_類似
 #       box.operator("mesh.select_similar", text="DIR").type='DIR' #_方向
        #3 - BOTTOM - RIGHT
   #     box = pie.split().column()
  #      row = box.row(align=True)
 #       box.operator("mesh.select_similar", text="NORMAL").type='NORMAL' #_ノーマル
#        box.operator("mesh.select_similar", text="LENGTH").type='LENGTH' #_長さ





#        pie.operator("view3d.select_circle", text="Circle Select", icon='BORDER_LASSO')

 #       pie.operator("mesh.select_similar")
#        pie.operator("mesh.select_all", text="De/Select All", icon='RENDER_REGION').action='TOGGLE'

#        pie.operator("mesh.loop_to_region", text="Region", icon='BORDER_LASSO')
#        pie.operator("mesh.loop_multi_select", text="Select Loop", icon='ZOOM_PREVIOUS').ring=False

# Pie Text Editor
class PieTextEditor(Menu):
    bl_idname = "pie.texteditor"
    bl_label = "Pie Text Editor"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        if bpy.context.area.type == 'TEXT_EDITOR':
            #4 - LEFT
            pie.operator("text.comment", text="Comment", icon='FONT_DATA')
            #6 - RIGHT
            pie.operator("text.uncomment", text="Uncomment", icon='NLA')
            #2 - BOTTOM
            pie.operator("wm.save_mainfile", text="Save", icon='FILE_TICK')
            #8 - TOP
            pie.operator("text.start_find", text="Search", icon='VIEWZOOM')
            #7 - TOP - LEFT
            pie.operator("text.indent", text="Tab (indent)", icon='FORWARD')
            #9 - TOP - RIGHT
            pie.operator("text.unindent", text="UnTab (unindent)", icon='BACK')
            #1 - BOTTOM - LEFT
            pie.operator("text.save", text="Save Script", icon='SAVE_COPY')
            #3 - BOTTOM - RIGHT

# Pie Animation
class PieAnimation(Menu):
    bl_idname = "pie.animation"
    bl_label = "Pie Animation"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("screen.animation_play", text="Reverse", icon='PLAY_REVERSE').reverse = True
        #6 - RIGHT
        if not context.screen.is_animation_playing:# Play / Pause
            pie.operator("screen.animation_play", text="Play", icon='PLAY')
        else:
            pie.operator("screen.animation_play", text="Stop", icon='PAUSE')
        #2 - BOTTOM
        #pie.operator(toolsettings, "use_keyframe_insert_keyingset", toggle=True, text="Auto Keyframe ", icon='REC')
        pie.operator("insert.autokeyframe", text="Auto Keyframe ", icon='REC')
        #8 - TOP
        pie.menu("VIEW3D_MT_object_animation", icon = "CLIP")
        #7 - TOP - LEFT
        pie.operator("screen.frame_jump", text="Jump REW", icon='REW').end = False
        #9 - TOP - RIGHT
        pie.operator("screen.frame_jump", text="Jump FF", icon='FF').end = True
        #1 - BOTTOM - LEFT
        pie.operator("screen.keyframe_jump", text="Previous FR", icon='PREV_KEYFRAME').next = False
        #3 - BOTTOM - RIGHT
        pie.operator("screen.keyframe_jump", text="Next FR", icon='NEXT_KEYFRAME').next = True

#Pie Save/Open
class PieSaveOpen(Menu):
    bl_idname = "pie.saveopen"
    bl_label = "Pie Save/Open"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        #4 - LEFT
        pie.operator("split.horizontal", text="Split Horizontal", icon= 'TRIA_DOWN')
#        pie.operator("wm.read_homefile", text="New", icon='NEW')

        #6 - RIGHT
        pie.operator("split.vertical", text="Split Vertical", icon= 'TRIA_RIGHT')
#        pie.operator("file.save_incremental", text="Incremental Save", icon='SAVE_COPY')

        #2 - BOTTOM
        pie.operator("area.joinarea", text="Split Horizontal", icon= 'TRIA_DOWN')

        #8 - TOP
        pie.operator("object.view_menu", text="NLA Editor", icon= 'NLA').variable="NLA_EDITOR"


        #7 - TOP - LEFT
        pie.operator("object.view_menu", text="Movie Clip Editor", icon= 'RENDER_ANIMATION').variable="CLIP_EDITOR"

        #9 - TOP - RIGHT
        box = pie.split().column()
        row = box.row(align=True)
        box.operator("import_scene.obj", text="Import OBJ", icon='IMPORT')
        box.operator("export_scene.obj", text="Export OBJ", icon='EXPORT')
        box.operator("import_scene.fbx", text="Import FBX", icon='IMPORT')
        box.operator("export_scene.fbx", text="Export FBX", icon='EXPORT')
        box.operator("object.view_menu", text="Outliner", icon= 'OOPS').variable="OUTLINER"

#         box = pie.split().column()
#         row = box.row(align=True)
#         box.operator("wm.recover_auto_save", text="Recover Auto Save...", icon='RECOVER_AUTO')
#         box.operator("wm.recover_last_session", text="Recover Last Session", icon='RECOVER_LAST')
#         box.operator("wm.revert_mainfile", text="Revert", icon='FILE_REFRESH')

#         box = pie.split().column()
#         row = box.row(align=True)
#         box.operator("wm.link", text="Link", icon='LINK_BLEND')
#         box.operator("wm.append", text="Append", icon='APPEND_BLEND')
#         box.menu("external.data", text="External Data", icon='EXTERNAL_DATA')
#         #1 - BOTTOM - LEFT
        pie.operator("object.view_menu", text="Sequence Editor", icon= 'SEQUENCE').variable="SEQUENCE_EDITOR"

#         #3 - BOTTOM - RIGHT
        pie.operator("object.view_menu", text="Python Console", icon= 'CONSOLE').variable="CONSOLE"


#Search Menu
def SearchMenu(self, context):
    layout = self.layout

    layout.operator("wm.search_menu", text="", icon ='VIEWZOOM')

def view3d_Search_menu(self, context):
    layout = self.layout

    layout.menu("SearchMenu")






# =====================================================
# =====================================================
#
# =====================================================
# =====================================================

# =====================================================
# =====================================================





addon_keymaps = []

def register():
    bpy.utils.register_module(__name__)


# Keympa Config

    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        #Select Mode
        km = wm.keyconfigs.addon.keymaps.new(name='Object Non-modal')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'RIGHTMOUSE', 'PRESS')
        kmi.properties.name = "pie.objecteditmode"

        #Views numpad
        # km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'Q', 'PRESS')
        # kmi.properties.name = "pie.viewnumpad"

        #Views
        km = wm.keyconfigs.addon.keymaps.new(name='Screen')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'Q', 'PRESS', ctrl=True)
        kmi.properties.name = "pie.areaviews"

        #Sculpt Pie Menu
        # km = wm.keyconfigs.addon.keymaps.new(name='Sculpt')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'W', 'PRESS')
        # kmi.properties.name = "pie.sculpt"

        #Sculpt Pie Menu 2
        # km = wm.keyconfigs.addon.keymaps.new(name='Sculpt')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'W', 'PRESS', alt=True)
        # kmi.properties.name = "pie.sculpttwo"

        #Origin/Pivot
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'RIGHTMOUSE', 'PRESS', alt=True)
        kmi.properties.name = "pie.originpivot"

        #Manipulators
        # km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'SPACE', 'PRESS', ctrl=True)
        # kmi.properties.name = "pie.manipulator"

        #Snapping
        # km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS', shift=True)
        # kmi.properties.name = "pie.snapping"

        #Orientation
        # km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'SPACE', 'PRESS', alt=True)
        # kmi.properties.name = "pie.orientation"

        #Shading
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'RIGHTMOUSE', 'PRESS', alt=True, shift=True)
        kmi.properties.name = "pie.shadingview"

        #Object shading
        km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'Z', 'PRESS', shift=True)
        kmi.properties.name = "pie.objectshading"

        #Pivot Point
        # km = wm.keyconfigs.addon.keymaps.new(name = '3D View Generic', space_type = 'VIEW_3D')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'Q', 'PRESS', alt=True)
        # kmi.properties.name = "pie.pivotpoint"

        #ProportionalEditObj
        # km = wm.keyconfigs.addon.keymaps.new(name = 'Object Mode')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'O', 'PRESS')
        # kmi.properties.name = "pie.proportional_obj"

        #ProportionalEditEdt
        # km = wm.keyconfigs.addon.keymaps.new(name = 'Mesh')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'O', 'PRESS')
        # kmi.properties.name = "pie.proportional_edt"

        #Align
        # km = wm.keyconfigs.addon.keymaps.new(name = 'Mesh')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'X', 'PRESS', alt=True)
        # kmi.properties.name = "pie.align"

        #Delete
        # km = wm.keyconfigs.addon.keymaps.new(name = 'Mesh')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'X', 'PRESS')
        # kmi.properties.name = "pie.delete"

        #Apply Transform
        # km = wm.keyconfigs.addon.keymaps.new(name = 'Object Mode')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'A', 'PRESS', ctrl=True)
        # kmi.properties.name = "pie.applytranforms"

        #Selection Object Mode
        km = wm.keyconfigs.addon.keymaps.new(name = 'Object Mode')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'G', 'PRESS', shift=True)
        kmi.properties.name = "pie.selectionsom"

        #Selection Edit Mode
        km = wm.keyconfigs.addon.keymaps.new(name = 'Mesh')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'G', 'PRESS', shift=True)
        kmi.properties.name = "pie.selectionsem"

        #Tex Editor
        # km = wm.keyconfigs.addon.keymaps.new(name = 'Text', space_type = 'TEXT_EDITOR')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'RIGHTMOUSE', 'PRESS', ctrl=True, alt=True)
        # kmi.properties.name = "pie.texteditor"

        #Animation
        # km = wm.keyconfigs.addon.keymaps.new(name='Object Non-modal')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'A', 'PRESS', alt=True)
        # kmi.properties.name = "pie.animation"

        #Save/Open/...
        # km = wm.keyconfigs.addon.keymaps.new(name='Window')
        # kmi = km.keymap_items.new('wm.call_menu_pie', 'S', 'PRESS', ctrl=True)
        # kmi.properties.name = "pie.saveopen"
        #
        # addon_keymaps.append(km)

# Register / Unregister Classes
def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
