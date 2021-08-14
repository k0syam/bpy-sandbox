import bpy
from datetime import timedelta

## add fonts if you intend to use them
# font_filepath = "specificfilepath.otf" 
# bpy.ops.font.open(font_filepath)

# settings

insertion_text = [
    {"text": "吾輩は猫である。名前はまだ無い。", "time":timedelta(minutes=0, seconds=1)},
    {"text": "どこで生れたかとんと見当がつかぬ。", "time":timedelta(minutes=0, seconds=2)},
    {"text": "何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。", "time":timedelta(minutes=0, seconds=3)},
    {"text": "吾輩はここで始めて人間というものを見た。", "time":timedelta(minutes=0, seconds=5)},
]

font_name = "Bfont"

# functions

def timedelta2frame(timedelta):
    fps = bpy.context.scene.render.fps
    return int(timedelta.seconds * fps)

def text_insertion(insertion_text):
    for i, chunk in enumerate(insertion_text):
        bpy.ops.object.text_add()
        bpy.data.objects[-1].data.body = chunk["text"]
        bpy.data.objects[-1].location = [0, 0, 0]
        bpy.data.objects[-1].data.font = bpy.data.fonts[font_name]
        bpy.data.objects[-1].hide_viewport = True
        bpy.data.objects[-1].hide_render = True        
        bpy.data.objects[-1].keyframe_insert(data_path='hide_viewport', frame=1)
        bpy.data.objects[-1].keyframe_insert(data_path='hide_render', frame=1)
        bpy.data.objects[-1].hide_viewport = False
        bpy.data.objects[-1].hide_render = False
        bpy.data.objects[-1].keyframe_insert(data_path='hide_viewport', frame=timedelta2frame(chunk["time"]))
        bpy.data.objects[-1].keyframe_insert(data_path='hide_render', frame=timedelta2frame(chunk["time"]))
        if i < len(insertion_text) - 1:
            bpy.data.objects[-1].hide_viewport = True
            bpy.data.objects[-1].hide_render = True
            bpy.data.objects[-1].keyframe_insert(data_path='hide_viewport', frame=timedelta2frame(insertion_text[i+1]["time"]))
            bpy.data.objects[-1].keyframe_insert(data_path='hide_render', frame=timedelta2frame(insertion_text[i+1]["time"]))
        fcurves = bpy.data.objects[-1].animation_data.action.fcurves
        for fcurve in fcurves:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = "CONSTANT"

text_insertion(insertion_text)
