import cut_png
import make_gif

frames, frame_duration = cut_png.cut_png()
make_gif.make_gif_import(frames, frame_duration)