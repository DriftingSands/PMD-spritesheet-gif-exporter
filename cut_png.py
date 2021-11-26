from PIL import Image, ImageChops
import glob
import xml.etree.ElementTree as ET
import math

def get_anim_info():
    tree = ET.parse('sprite-sheet/animations.xml')
    root = tree.getroot()
    width = int(root.find('FrameWidth').text)
    height = int(root.find('FrameHeight').text)
    anim_group_table = root.find('AnimGroupTable')
    # print('anim group table', anim_group_table)

    anim_index = int(anim_group_table[1][7].text)

    anim_seq_table = root.find('AnimSequenceTable')
    anim_seq = anim_seq_table[anim_index]
    # print(ET.tostring(anim_seq))

    anim_info = []
    for element in anim_seq.findall('AnimFrame'):
        duration = int(element.find('Duration').text)
        sheet_frame = int(element.find('MetaFrameGroupIndex').text)
        sprite_offset_x = int(element.find('Sprite')[0].text)
        sprite_offset_y = int(element.find('Sprite')[1].text)
        flip = int(element.find('HFlip').text)
        
        anim_info.append([sheet_frame, duration, sprite_offset_x, sprite_offset_y, flip])
    # print(anim_info)
    return [width, height, anim_info]

def cut_png():
    sprite_info = get_anim_info()
    sheet = Image.open('sprite-sheet/sheet.png')
    print(sheet.width)
    width, height, anim_info = sprite_info
    print(width, height, anim_info)
    frames = []
    frame_duration = []
    for element in anim_info:
        remainder = (math.floor((width * element[0]) / sheet.width))
        to_remove = remainder * sheet.width

        startX = (width * element[0]) - to_remove
        endX = startX + width
        # adjust Y, its hardcoded for now
        startY = remainder * height
        print(startY)
        endY = startY + height

        img = sheet.crop((startX, startY, endX, endY))
        img = ImageChops.offset(img, element[2], element[3])
        if element[4] == 1:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)

        frames.append(img)
        frame_duration.append(element[1])
    return (frames, frame_duration)

# cut_png()




# 32 x 42