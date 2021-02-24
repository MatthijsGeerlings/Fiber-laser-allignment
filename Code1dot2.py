'Function based on idea 1.2 see notebook'

def find_fiber_center_code1_dot_2(filename,n_value=0.001):
    'The n_value is put on 0.001 by default, which for now seems to be the best value'
    import PIL
    import os
    import numpy as np
    
    'The line of code below, splits the filename into its name and its extention (including the .)'
    fn, fext = os.path.splitext(filename)
    'If the code is run on an npy file, the images are created in the 4 lines of code below'
    if fext == '.npy':
        img_array = np.load(filename)
        Image = PIL.Image.fromarray(img_array)
        Image2 = PIL.Image.fromarray(img_array)
    else:
        Image = PIL.Image.open(filename)
        Image2 = PIL.Image.open(filename)

    f = Image.load()
    
    'A list of all pixel (brightness) values is created below'
    pixel_values = []
    for i in range(Image.size[0]):
        for j in range(Image.size[1]):
            pixel_values.append(f[i,j])
        
    'The line of code below oreders the list pixel_values from small to large'        
    pixel_values = sorted(pixel_values)

    '''The line of code below determines the threshold value for which pixels should and shouldn't 
    be considert 'bright' '''
    threshold = pixel_values[int(len(pixel_values)*(1-n_value))]

    'The lines of code below put the outer most pixels in the figure to 0'
    for i in range(Image.size[0]):
        Image.putpixel((i,0),(0))
        Image.putpixel((i,Image.size[1]-1),(0))
    for i in range(Image.size[1]):
        Image.putpixel((0,i),(0))
        Image.putpixel((Image.size[0]-1,i),(0))
    
    
    '''Below a list of coodinates of bright pixel values is created'''
    bright_coords = []
    for i in range(Image.size[0]):
        for j in range(Image.size[1]):
            if f[i,j]>threshold:
                bright_coords.append([i,j])
    
    
    bright_neighbors_required = 4         
    
    ''''In the while loop below, the bright pixels with non bright neibours keep getting removed 
    until their are only pixels with non bright neighbours left'''
    while len(bright_coords) > 1:

        '''The list 'removers' contains the pixel coordinates of the pixels that are going to be put to
        zero, these pixels will also be removed from the list btight_coords'''
        removers = []
        for i in bright_coords:
            bright_neighbors = 0
            if f[i[0]-1,i[1]]>threshold:
                bright_neighbors = bright_neighbors + 1
            if f[i[0]+1,i[1]]>threshold:
                 bright_neighbors = bright_neighbors + 1
            if f[i[0],i[1]-1]>threshold:
                 bright_neighbors = bright_neighbors + 1
            if f[i[0],i[1]+1]>threshold:
                 bright_neighbors = bright_neighbors + 1
            
            if bright_neighbors < bright_neighbors_required:
                removers.append(i)
        
        '''The two lines of code below are to ensure the code does not hang'''
        if len(removers) <0.5:
            threshold = threshold+1
          
        '''When allow_remove =1, pixels are allowed to be removed for bright_coords, when 
        allow_remove = 0, they are not allowed to be removed'''
        allow_remove = 1
        
        '''When len(bright_coords)==len(removers) their is a break command, since you don't 
        want to end up with a empty list of bright pixel coordinates'''    
        if len(bright_coords)==len(removers):
            bright_neighbors_required = bright_neighbors_required - 1
            allow_remove = 0
    
        '''When bright_neighbors_required becomes zero, the algorithm is finished and the break
        forces am exit from the while loop'''
        if bright_neighbors_required<0.5:
            break
    
        if allow_remove>0.5:
            for i in removers:
                bright_coords.remove(i)
                Image.putpixel((i[0],i[1]),(0))
    
    
    'List of x coordinates of the brightest pixels that where left over'        
    x_coords = []   
    'List of y coordinates of the brightest pixels that where left over'
    y_coords = []

    for i in bright_coords:
        x_coords.append(i[0])
        y_coords.append(i[1])
    '''Determening the x and y coordinate of the core, by calculating the average coordinate for 
    both x and y (the +0.5 is added, to round the value to the closest integer instead of the one
    below it)'''
    x_coord_core = int(sum(x_coords)/len(x_coords)+0.5)
    y_coord_core = int(sum(y_coords)/len(y_coords)+0.5)

    'Mark the middle in Image2'
    for i in range(Image2.size[1]):
        Image2.putpixel((x_coord_core,i),(255))
    
    for i in range(Image2.size[0]):
        Image2.putpixel((i,y_coord_core),(255))
    return(Image2)