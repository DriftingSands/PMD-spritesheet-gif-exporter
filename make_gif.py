from PIL import Image
import glob



def make_gif_import(input_frames, input_frame_duration):
    frames = []
    # imgs = glob.glob('sprite-sheet/output/*.png')
    duration_index = 0
    for element in input_frames:
        new_frame = element
        width, height = new_frame.size
        width = width * 4
        height = height * 4
        new_frame = new_frame.resize((width, height), Image.NEAREST)
        new_frame.convert('RGBA')
        for i in range(input_frame_duration[duration_index]):
            frames.append(new_frame)
        duration_index += 1
    # frames[1].show()

    frames[0].save('png_to_gif.webp', format='WebP',
        save_all=True, append_images=frames[1:],
        duration=17, loop=0,
        disposal=2,
        # background=(255, 0, 255, 0),
        # version='GIF89a',
    )

