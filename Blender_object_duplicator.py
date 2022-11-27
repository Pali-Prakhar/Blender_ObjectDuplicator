import bpy

re = bpy.context.active_object
C = bpy.context
src_obj = bpy.data.objects['Source Object Name here']

for i in range (0,1):
    new_obj = src_obj.copy()
    new_obj.data = src_obj.data.copy()
    new_obj.animation_data_clear()
    C.collection.objects.link(new_obj)
    bpy.context.view_layer.objects.active = new_obj
    new_obj.location = re.location.copy()
    new_obj.rotation_euler = re.rotation_euler.copy()