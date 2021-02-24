'test'

def find_fiber_center_code1_dot_1(filename,n_value=0.001):
    import PIL
    Image = PIL.Image.open(filename)
    Image2 = PIL.Image.open(filename)

    f = Image.load()
    pixel_values = []
    for i in range(Image.size[0]):
        for j in range(Image.size[1]):
            pixel_values.append(f[i,j])
        
    'The line of code below oreders the list pixel_values from small to large'        
    pixel_values = sorted(pixel_values)

    '''The line of code below determines the threshold value for which pixels should and shouldn't be
    considert 'bright' '''
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
            
    ''''In the while loop below, the bright pixels with non bright neibours keep getting removed until
    their are less then 1.5 bright pixels left'''
    while len(bright_coords) > 1:
    
        '''The variable previous_bright_coords remembers the list bright_coords 
        before removing elements'''
        if len(bright_coords)>2:
            previous_bright_coords = bright_coords 
            print(len(bright_coords))
    
        '''The list 'removers' contains the pixel coordinates of the pixels that are going to be put to zero,
        these pixels will also be removed from the list btight_coords'''
        removers = []
        for i in bright_coords:
            if f[i[0]-1,i[1]]<threshold or f[i[0]+1,i[1]]<threshold or f[i[0],i[1]-1]<threshold or f[i[0],i[1]+1]<threshold:
                    removers.append(i)
                
        if len(bright_coords)==len(removers):
            break
    
        for i in removers:
            bright_coords.remove(i)
            Image.putpixel((i[0],i[1]),(0))
    
    
    'List with all the brightest pixels that where left over'        
    x_coords = []   
    y_coords = []

    if len(bright_coords) == 0:
        for i in previous_bright_coords:
            x_coords.append(i[0])
            y_coords.append(i[1])
        

    for i in bright_coords:
        x_coords.append(i[0])
        y_coords.append(i[1])
    

    x_coord_core = int(sum(x_coords)/len(x_coords)+0.5)
    y_coord_core = int(sum(y_coords)/len(y_coords)+0.5)

    'Mark the middle in Image2'
    for i in range(Image2.size[1]):
        Image2.putpixel((x_coord_core,i),(255))
    
    for i in range(Image2.size[0]):
        Image2.putpixel((i,y_coord_core),(255))
    return(Image2)