from PIL import Image, ImageFilter, ImageEnhance, ImageOps

def get_image_mode(img):
    return img.mode

def red_pixel_count(img):
    '''Get Red pixel count where red = 255'''
    red_pixel = 0
    for pixel in img.getdata():
        if pixel[0] == 255:
            red_pixel += 1
    return red_pixel

def convert2gray(img):
    return img.convert('L')

def dom_primarycolor(img, threshold=30):
    '''Gives dominant primary color
    Only counts pixels where one channel is significantly higher than the others
    threshold: minimum difference required between max channel and other channels
    '''
    red_pixel_count = 0
    blue_pixel_count = 0
    green_pixel_count = 0
    gray_pixel_count = 0

    for rgb in img.getdata():
        r, g, b = rgb
        max_val = max(r, g, b)
        min_val = min(r, g, b)
        
        # If all channels are similar (grayscale), skip this pixel
        if max_val - min_val < threshold:
            gray_pixel_count += 1
            continue
        
        # Find which channel is dominant
        if r == max_val and r - g >= threshold and r - b >= threshold:
            red_pixel_count += 1
        elif g == max_val and g - r >= threshold and g - b >= threshold:
            green_pixel_count += 1
        elif b == max_val and b - r >= threshold and b - g >= threshold:
            blue_pixel_count += 1

    color_list = [red_pixel_count, green_pixel_count, blue_pixel_count]
    
    # If all counts are zero (all pixels are grayscale), return gray
    if sum(color_list) == 0:
        return 'gray/neutral'
    
    dom_color_pos = color_list.index(max(color_list))

    if dom_color_pos == 0:
        return 'red'
    elif dom_color_pos == 1:
        return 'green'
    elif dom_color_pos == 2:
        return 'blue'

def dom_secondarycolor(img):
    '''Gives dominant secondary color (most frequent RGB tuple)'''
    color_dict = {}

    for rgb in img.getdata():
        if rgb not in color_dict:
            color_dict[rgb] = 1
        else:
            color_dict[rgb] += 1
    
    dom_color = max(color_dict, key=color_dict.get)
    return str(dom_color)

def create_color_swatch(rgb, size=(150, 100)):
    '''Creates a color swatch image from RGB tuple'''
    return Image.new('RGB', size, rgb)

def apply_transformation(img, transformation):
    '''Apply the selected transformation to the image'''
    
    if transformation == "Grayscale":
        return img.convert('L').convert('RGB')
    
    elif transformation == "Blur":
        return img.filter(ImageFilter.GaussianBlur(radius=5))
    
    elif transformation == "Sharpen":
        return img.filter(ImageFilter.SHARPEN)
    
    elif transformation == "Edge Detection":
        return img.filter(ImageFilter.FIND_EDGES)
    
    elif transformation == "Flip Horizontal":
        return img.transpose(Image.FLIP_LEFT_RIGHT)
    
    elif transformation == "Flip Vertical":
        return img.transpose(Image.FLIP_TOP_BOTTOM)
    
    elif transformation == "Rotate 90°":
        return img.rotate(90, expand=True)
    
    elif transformation == "Rotate 180°":
        return img.rotate(180)
    
    elif transformation == "Brightness Increase":
        enhancer = ImageEnhance.Brightness(img)
        return enhancer.enhance(1.5)
    
    elif transformation == "Brightness Decrease":
        enhancer = ImageEnhance.Brightness(img)
        return enhancer.enhance(0.5)
    
    elif transformation == "Contrast Increase":
        enhancer = ImageEnhance.Contrast(img)
        return enhancer.enhance(2.0)
    
    elif transformation == "Contrast Decrease":
        enhancer = ImageEnhance.Contrast(img)
        return enhancer.enhance(0.5) 
    
    elif transformation == "Invert":
        return ImageOps.invert(img)
    
    elif transformation == "Emboss":
        return img.filter(ImageFilter.EMBOSS)
    
    else:
        return img