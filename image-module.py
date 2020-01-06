#
# ps7pr5.py  (Problem Set 7, Problem 5)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

def grayscale(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list of pixels for an image that is a grayscale version of the original image"""
    x = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            x[r][c] = [brightness(pixels[r][c]),brightness(pixels[r][c]),brightness(pixels[r][c])]
    return x 

def fold_diag(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list"""
    x = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
                if r > c:
                    x[r][c] = [255, 255, 255]
                else:
                    x[r][c] = pixels[r][c]
    return x

def mirror_horiz(pixels):
    """takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list of pixels for an image in which the original image is “mirrored” horizontally"""
    x = blank_image(len(pixels),len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])): 
           if c >= len(pixels[0]) // 2:
               x[r][c] = pixels[r][(c+1)*-1]
           else:
               x[r][c] = pixels[r][c]
    return x 

def extract(pixels, rmin, rmax, cmin, cmax):
    """ takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list that represents the portion of the original image that is specified by the other four parameters"""
    x = blank_image(rmax-rmin,cmax-cmin)
    for r in range(rmax-rmin):
        for c in range(cmax-cmin): 
            x[r][c] = pixels[rmin + r][cmin + c]
    return x 
    
            
            
            
    
    


            
            
    

## put your functions below
