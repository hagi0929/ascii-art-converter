import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy

number_to_draw = ''
Ascii_lst = ' .,-~:;=!*#$@'  # 15
number_of_letters_y = 50  # display width size
img_array = []
vid = cv2.VideoCapture('./sample/sample_img_1.jpg')
total_frame = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
fps = vid.get(cv2.CAP_PROP_FPS)
original_width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
original_height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
ratio = original_width / original_height
number_of_letters_x = int(ratio * number_of_letters_y)
letter_ratio = number_of_letters_x / number_of_letters_y

fontsize = int(original_width / number_of_letters_y)
resolution = (int(number_of_letters_x * fontsize), int(number_of_letters_y * fontsize))   # x,y

image_background = "black"
font = ImageFont.truetype('./fonts/font.ttf', fontsize)


for i in range(total_frame):
    ret, img = vid.read()
    img = cv2.resize(img, (number_of_letters_x * 2, number_of_letters_y))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (number_of_letters_x * 2, number_of_letters_y))

    im = Image.new("L", resolution, image_background)
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(number_to_draw)
    for y, row in enumerate(img):
        for x, pixel in enumerate(row):
            chooser = int(pixel / 256 * 13)
            draw.text((x * fontsize / 2, y * fontsize), Ascii_lst[chooser], font=font, fill='#FFFFFF')
    img_array.append(cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR))
    print(f'{total_frame}/{i+1}')

out = cv2.VideoWriter('project2.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps=fps, frameSize=resolution)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()