import cut_png
import make_gif
import glob

pokemon_dir = glob.glob('pmd_monster/*/')


for element in pokemon_dir:
    name = element.split('pmd_monster\\')[1]
    name = name.split('_')
    if len(name) == 2:
        name = name[0][0:3] + '_' + name[1]
        name = name[:-1]
    else:
        name = name[0][0:3]

    # pass (animation, direction, directory)
    frames, frame_duration = cut_png.cut_png(1, 7, element)
    make_gif.make_gif_import(frames, frame_duration, name)
