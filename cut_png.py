from PIL import Image
import glob
import xml.etree.ElementTree as ET

tree = ET.parse('sprite-sheet/animations.xml')
root = tree.getroot()
width = int(root.find('FrameWidth').text)
height = int(root.find('FrameHeight').text)
anim_group_table = root.find('AnimGroupTable')
print(anim_group_table)

anim_index = int(anim_group_table[1][0].text)
print(anim_index)

anim_seq_table = root.find('AnimSequenceTable')
anim_seq = anim_seq_table[anim_index]
# print(ET.tostring(anim_seq))

anim_info = []
for element in anim_seq.findall('AnimFrame'):
    print(element)

def cut_png():
    sheet = Image.open('sprite-sheet/sheet.png')
    width, height = sheet.size
    original_width = width / 7
    original_height = height / 7
    width = original_width
    height = original_height
    startX = 0
    startY = 0
    frames = []
    for element in range(7):
        img = sheet.crop((startX, startY, width, height))
        frames.append(img)
        startX += original_width
        width += original_width
    return frames

# cut_png()




# 32 x 42