import bpy


# settings

location_sequence = [
    {
     "name": "Light",
     "beat": [0, 1/4, 2/4, 3/4, 4/4],
     "location_x": [5, 5, -5, -5, 5],
     "location_y": [5, -5, -5, 5, 5],
     "location_z": [5, 5, 5, 5, 5],
     },
]

bpm = 97

# functions

# this is under 4/4 tempo
def beat2frame(beat=1/4, bpm=bpm):
    fps = bpy.context.scene.render.fps
    frames_per_bar = 4 * fps / bpm * 60
    return int(frames_per_bar * beat + 1)

def insert_location(obj, location=[0.0, 0.0, 0.0], frame=1):
    obj.location = location
    obj.keyframe_insert(data_path='location', frame=frame)

def object_move(loc_seq, bpm):
    for obj_selected in loc_seq:
        obj = bpy.data.objects[obj_selected["name"]]
        for i, beat in enumerate(obj_selected["beat"]):
            current_loc = [obj_selected["location_x"][i], obj_selected["location_y"][i], obj_selected["location_z"][i]]
            if beat == 0:
                insert_location(obj, current_loc, frame=1)
            else:
                insert_location(obj, current_loc, frame=beat2frame(beat))
        fcurves = obj.animation_data.action.fcurves
        for fcurve in fcurves:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = "LINEAR"

object_move(location_sequence, bpm)
