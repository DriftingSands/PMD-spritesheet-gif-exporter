import cut_png
import make_gif
import glob

pokemon_dir = glob.glob('pmd_monster/*/')

for element in pokemon_dir:
    name = element[12:15]

    # pass (animation, direction, directory)
    frames, frame_duration = cut_png.cut_png(1, 7, element)
    make_gif.make_gif_import(frames, frame_duration, name)
