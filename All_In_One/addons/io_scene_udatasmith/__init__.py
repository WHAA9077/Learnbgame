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

# <pep8 compliant>

bl_info = {
    "name": "Unreal Datasmith format",
    "author": "Andres Botero",
    "blender": (2, 80, 0),
    "location": "File > Export > Datasmith (.udatasmith)",
    "description": "Export scene as Datasmith asset",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
                "Scripts/Import-Export/DSM",
    "category": "Learnbgame",
}

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# To support reload properly, try to access a package var,
# if it's there, reload everything
if "bpy" in locals():
    import importlib
    if "export_datasmith" in locals():
        importlib.reload(export_datasmith)
    if "import_datasmith" in locals():
        importlib.reload(import_datasmith)



import bpy
from bpy.props import (
        StringProperty,
        BoolProperty,
        FloatProperty,
        EnumProperty,
        )
from bpy_extras.io_utils import (
        ImportHelper,
        ExportHelper,
        path_reference_mode,
        axis_conversion,
        )

class ExportDatasmith(bpy.types.Operator, ExportHelper):
    """Write a Datasmith file"""
    bl_idname = "export_scene.datasmith"
    bl_label = "Export Datasmith"
    bl_options = {'UNDO', 'PRESET'}

    filename_ext = ".udatasmith"
    filter_glob: StringProperty(default="*.udatasmith", options={'HIDDEN'})

    def draw(self, context):
        layout = self.layout

        layout.prop(self, "version")
        layout.prop(self, "use_selection")
        layout.prop(self, "global_scale")
        layout.prop(self, "include_metadata")
        layout.prop(self, "embed_textures")
        layout.prop(self, "batch_mode")


    def execute(self, context):
        keywords = self.as_keywords(ignore=("filter_glob",))
        from . import export_datasmith
        return export_datasmith.save(self, context, **keywords)

def menu_func_export(self, context):
    self.layout.operator(ExportDatasmith.bl_idname, text="Datasmith (.udatasmith)")

classes = (
    ExportDatasmith,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
