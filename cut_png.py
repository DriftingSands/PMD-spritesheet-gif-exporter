from PIL import Image, ImageChops
import glob
import xml.etree.ElementTree as ET

def get_anim_info():
    tree = ET.parse('sprite-sheet/animations.xml')
    root = tree.getroot()
    width = int(root.find('FrameWidth').text)
    height = int(root.find('FrameHeight').text)
    anim_group_table = root.find('AnimGroupTable')
    # print('anim group table', anim_group_table)

    anim_index = int(anim_group_table[1][0].text)
    # Remove this later, I didn't zero index while counting in my head for testing =)
    anim_index += 1
    # print('anim index', anim_index)

    anim_seq_table = root.find('AnimSequenceTable')
    anim_seq = anim_seq_table[anim_index]
    # print(ET.tostring(anim_seq))

    anim_info = []
    for element in anim_seq.findall('AnimFrame'):
        duration = int(element.find('Duration').text)
        sheet_frame = int(element.find('MetaFrameGroupIndex').text)
        sprite_offset_x = int(element.find('Sprite')[0].text)
        sprite_offset_y = int(element.find('Sprite')[1].text)
        
        anim_info.append([sheet_frame, duration, sprite_offset_x, sprite_offset_y])
    # print(anim_info)
    return [width, height, anim_info]

def cut_png():
    sprite_info = get_anim_info()
    sheet = Image.open('sprite-sheet/sheet.png')
    width, height, anim_info = sprite_info
    print(width, height, anim_info)
    frames = []
    frame_duration = []
    for element in anim_info:
        startX = width * element[0]
        endX = startX + width
        # adjust Y, its hardcoded for now
        startY = 0
        endY = startY + height

        img = sheet.crop((startX, startY, endX, endY))
        img = ImageChops.offset(img, element[2], element[3])
        frames.append(img)
        frame_duration.append(element[1])
    return (frames, frame_duration)

# cut_png()




# 32 x 42