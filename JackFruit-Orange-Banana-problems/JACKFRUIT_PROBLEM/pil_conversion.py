from PIL import Image

def get_image_mode(img):
  img_mode = img.mode
  return img_mode

def red_pixel_count(img):
  '''Get Red pixel count'''
  red_pixel = 0
  for pixel in img.getdata():
    if pixel[0] == 255:
      red_pixel +=1
  return red_pixel

def convert2gray(img):
  return img.convert('L')


def dom_primarycolor(img):
  '''Gives dominant primary color'''
  red_pixel_count = 0
  blue_pixel_count = 0
  green_pixel_count = 0

  for rgb in img.getdata():

    index = rgb.index(max(rgb))
    if index == 0:
      red_pixel_count = red_pixel_count + 1
    elif index == 1:
      green_pixel_count = green_pixel_count + 1  
    elif index == 2:
      blue_pixel_count = blue_pixel_count + 1

  color_list = [red_pixel_count,green_pixel_count,blue_pixel_count]
  dom_color_pos= color_list.index(max(color_list))

  if dom_color_pos == 0:
    return 'red'
  elif dom_color_pos == 1:
    return 'green'
  elif dom_color_pos == 2:
    return 'blue'
  
def create_color_swatch(rgb, size=(100, 50)):
    return Image.new('RGB', size, rgb)

# def dom_secondarycolor(img):
#     '''Gives dominant secondary color'''

#     color_dict = {}
#     for rgb in img.getdata():
#       if rgb not in color_dict:
#         color_dict[rgb] = 1
#       else:
#         color_dict[rgb] += 1
    
#     sorted_colors = sorted(color_dict.items(), key=lambda x: x[1], reverse=True)

#     # for color, count in sorted_colors[:3]:
#     #     print(f"  {color}: {count} pixels")
    
#     dom_color = max(color_dict, key=color_dict.get)
#     return dom_color, sorted_colors


def dom_secondarycolor(img):
  '''Gives dominant secondary color'''
  color_dict = {}

  for rgb in img.getdata():

    if rgb not in color_dict:
      color_dict[rgb] = 1
    else:
      color_dict[rgb] += 1
  
  dom_color = str(max(color_dict, key=color_dict.get))

  return dom_color