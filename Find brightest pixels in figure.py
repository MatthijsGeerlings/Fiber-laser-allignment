''''Find brightest pixels in figure'''
import PIL
import os

def mark_spots_with_brightest_pixels(filename):
    import PIL
    Image = PIL.Image.open(filename)
    f = Image.load()
    pixel_values = []
    for i in range(Image.size[0]):
        for j in range(Image.size[1]):
            pixel_values.append(f[i,j])
    max_value = max(pixel_values)
    
    'x_coords and y_coords below represent the x and y coordinates of the brightest pixels'
    x_coords = []
    y_coords = []
    
    for i in range(Image.size[0]):
        for j in range(Image.size[1]):
            if f[i,j] == max_value:
                x_coords.append(i)
                y_coords.append(j)
                
    for i in x_coords:
        for j in range(Image.size[1]):
            Image.putpixel((i,j),(255))
            
    for j in y_coords:
        for i in range(Image.size[0]):
            Image.putpixel((i,j),(255))
    
    return Image
                
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = mark_spots_with_brightest_pixels(f)
        j = PIL.Image.open(f)
        fn, fext = os.path.splitext(f)
        j.save('brightest_spots_marked\{}.jpg'.format(fn))
        i.save('brightest_spots_marked\{}_brightest_spots_marked.jpg'.format(fn))