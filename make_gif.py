from PIL import Image
import math
import pathlib


def make_gif_import(input_frames, input_frame_duration, name):
    frames = []
    
    # lowering amount of duplicate frames
    if input_frame_duration.count(input_frame_duration[0]) == len(input_frame_duration):
        greatest_frame_div = input_frame_duration[0]
    else:
        greatest_frame_div = math.gcd(*input_frame_duration)
    for i in range(len(input_frame_duration)):
        input_frame_duration[i] = int(input_frame_duration[i] / greatest_frame_div)

    duration_index = 0
    for element in input_frames:
        new_frame = element
        width, height = new_frame.size
        width = width * 4
        height = height * 4
        new_frame = new_frame.resize((width, height), Image.NEAREST)
        '''
        extra for trying to get GIF to work... it just wont, I'm sticking wo WEBP

        alpha = new_frame.split()[3]
        new_frame = new_frame.convert('RGB').convert('P', palette=Image.ADAPTIVE)
        mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)
        new_frame.paste(255, mask)
        '''

        for i in range(input_frame_duration[duration_index]):
            frames.append(new_frame)
        duration_index += 1
    # frames[1].show()

    path = pathlib.Path().resolve()
    # if name == '006':
    #     print(input_frame_duration)
    #     print(17*greatest_frame_div)

    frames[0].save(f'{path}/output/{name}.webp', format='webp',
        save_all=True, append_images=frames[1:],
        duration=(17*greatest_frame_div), loop=0,
        disposal=2,
        transparency=255,
        # background=(255, 0, 255, 255),
        # version='GIF89a',
    )
    # new_gif = Image.open(f'{path}/output/{name}.webp')
    # new_gif.save(f'{path}/output/{name}.gif', format='gif',
    #     save_all=True, 
    #     duration=(17*greatest_frame_div), loop=0,
    #     # disposal=2,
    #     # transparency=8
        # )

