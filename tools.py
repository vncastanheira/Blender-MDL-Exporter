import bpy

def add_menu_item(self, context):
    self.layout.label("Added this line")
    self.layout.operator("mesh.select_similar_kcl_flags")

bpy.types.VIEW3D_MT_edit_mesh_select_similar.append(add_menu_item)