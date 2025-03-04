'''
Copyright (C) 2015 Keys Addon
diego@sinestesia.co

Created by Diego Gangl

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Keys Reflow",
    "description": "Recalculate keyframes for different fps",
    "author": "Diego Gangl <diego@sinestesia.co>",
    "version": (0, 1, 0),
    "blender": (2, 75, 0),
    "location": "Properties > Render",
    "wiki_url": "",
    "category": "Learnbgame",
}
    
    
import bpy      


# load and reload submodules
##################################    
    
from . import developer_utils
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())



# register
################################## 

import traceback

def register():
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()
    
    print("Registered {} with {} modules".format(bl_info["name"], len(modules)))
    
    bpy.types.RENDER_PT_dimensions.append(reflow.render_button)
    
def unregister():
    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()
    
    print("Unregistered {}".format(bl_info["name"]))
