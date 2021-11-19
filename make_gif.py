from PIL import Image
import glob



def make_gif_import(input):
    frames = []
    # imgs = glob.glob('sprite-sheet/output/*.png')
    for element in input:
        new_frame = element
        width, height = new_frame.size
        width = width * 4
        height = height * 4
        new_frame = new_frame.resize((width, height), Image.NEAREST)
        new_frame.convert('RGBA')
        frames.append(new_frame)
    # frames[1].show()

    frames[0].save('png_to_gif.webp', format='WebP',
        save_all=True, append_images=frames[1:],
        duration=150, loop=0,
        disposal=2,
        # background=(255, 0, 255, 0),
        # version='GIF89a',
    )

