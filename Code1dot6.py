
'Code 1.6'
''' In this function, the numpy array is multplied with a matrix that decreases the pixel value by a
factor depending on the distance from the middle of the image array (the closer to the edge,
the bigger is the decrease). This function yields good results'''

def code1dot6(npy_file,n_value = 0.001):
    '''With this code the core can be found within 100 ms (if the image is not extremely pore).
    In this function, the numpy array is multplied with a matrix that decreases the pixel value by a
    factor depending on the distance from the middle of the image array (the closer to the edge,
    the bigger is the decrease). On this array, basically the same algorithm as in code 1.2 
    (see below) is perforemd. In this code however some functions from existing Python libaries 
    are used to speed up the process (especially the numpy function percentille speeds up the 
    function a lot)
    
    Code 1.2 is based on the same principle as code 1.1 (see description below). In code 1.2
    however, the code is not stopped when there is no more pixel with 4 bright neighbors, but
    the threshold of required bright neighbors is lowerd to 3 (then to 2 and then to 1). The pixels
    that are still present when a value of 0 (for bright neighbors required) is reached, determine
    the coordinates of the core.
    
    The n_value is put on 0.001 by default, which for now seems to be the best value
    
    Code 1.1: This function is based on the idea, taht the core is the area in the picture with the most
    'bright' pixels, the n_value determines which part of the pixels should be considerd bright.
    When, for example, n_value=0.1, the 10% brightest pixels are considerd bright. 
    The way the function works, is that bright pixels are keep being removed from the picture, 
    if they have less than 4 bright (direct) neighbours. The pixel(s) that are left over at the end,
    determine the coordinates of the core. The n_value is put on 0.001 by default, which for 
    now seems to be the best value'''
    
    'required imports'
    import time
    from numpy import percentile, where, load, linspace
    from copy import copy
    import PIL
 
    '''Below the multiplication array is defined (when implementing this code, it will be 
    saved somewhere and loaded when needed)'''
    multiply_array = (linspace(2,0,960*1280).reshape(1280,960)*\
        linspace(0,2,960*1280).reshape(1280,960))**8
    
        
    time_one = time.time()
    
    'Loading of npy_file'
    np_array_original = load(npy_file)
    
    '''Below 'array' is created, which is the product of the multiply_array and the original array'''
    array = (np_array_original*multiply_array).astype(int)
    
    'Determination of the threshold value'
    threshold = round(percentile(array,(100-(100*n_value)),interpolation='nearest'))

    ''' Below a binary array is created, pixels above the threshold get assigned the value 1 and 
    pixels below the threshold get assigned the value 0'''
    np_array_binary = where(array>threshold,1,0)

    'The lines of code below put the edges of the image to 0'
    'Puts the top column to 0'
    np_array_binary[0,:] = 0 
    'Puts the lowest column to 0'
    np_array_binary[-1,:] = 0
    'Puts the left column to zero'
    np_array_binary[:,0] = 0
    'Puts the right column to zero'
    np_array_binary[:,-1] = 0    

    'Determination of the bright pixel locations'
    bright_pixel_locations = where(np_array_binary == 1)

    'List containing the bright pixel coordinates'
    bright_coords = []

    'Filling the list of bright pixel coordinates'
    for i in range(0,len(bright_pixel_locations[0])):
         bright_coords.append([bright_pixel_locations[0][i],bright_pixel_locations[1][i]])
   
    
    ''''Variable required in while loop, so the function does not hang, reason for assigning the 
    value -1, is so, the if statement: 
        if previous_length_bright_coords == len(bright_coords_copy)
    can never be 'True' during the first itteration in the while loop. '''
    previous_length_bright_coords = -1
    

    'Number of bright neighbors required'
    bright_negihbors_required = 4
    
    'In this while loop, the determination of the pixels at the fiber core is done'
    while len(bright_coords)>=1:
        
        'Copy of the binary array'
        binary_copy = copy(np_array_binary)
        bright_coords_copy = copy(bright_coords)
    
        'In this for loop, for eacht pixel the number of bright (direct) neighbors is determined'
        for i in bright_coords:
            bright_neighbors = 0
            if np_array_binary[i[0]-1][i[1]] == 1:
                bright_neighbors = bright_neighbors+1
            if np_array_binary[i[0]+1][i[1]] == 1:
                bright_neighbors = bright_neighbors+1
            if np_array_binary[i[0]][i[1]-1] == 1:
                bright_neighbors = bright_neighbors+1
            if np_array_binary[i[0]][i[1]+1] == 1:
                bright_neighbors = bright_neighbors+1
        
            'If a pixel has less bright neighbors than required, it is put to 0 '
            if bright_neighbors<bright_negihbors_required:
                binary_copy[i[0]][i[1]] = 0
                bright_coords_copy.remove(i)
            else:
                pass
    
    
        '''If nothing is added to the list bright_coords_copy, the threshold for required bright 
        neighbors is lowered, and both the binary array as the bright coords list are kept the same
        '''
        if len(bright_coords_copy) <0.5:
            bright_negihbors_required = bright_negihbors_required -1
        else:
            np_array_binary = binary_copy
            bright_coords = bright_coords_copy
        
        'When there is no more pixel with any bright neighbors, break'
        if bright_negihbors_required<0.5:
            break
        
        
        if previous_length_bright_coords == len(bright_coords_copy):
            ''''When pixels are no longer being removed, the itteration is stopped with the break 
        commend'''
            break
        
        'Number of bright coordinates during the previous round through the while loop'
        previous_length_bright_coords = len(bright_coords)
        
        
    'Determening x- and y coordinate core'
    x = 0
    y = 0
    for i in bright_coords:
        x = x + i[1]
        y = y + i[0]
    x = round(x/len(bright_coords))
    y = round(y/len(bright_coords))
    print(x,y)
    print('Time required to find core',round(1000*(time.time()-time_one)),'ms')
    #return([x,y])  

    'Creating image with the core marked'
    Image = PIL.Image.fromarray(load(npy_file))
    for i in range(Image.size[1]):
        Image.putpixel((x,i),(255))
    
    for i in range(Image.size[0]):
        Image.putpixel((i,y),(255))
    #Image.show()
    return(Image)
'Performing the protocol on every numpy array in the map'
import os
import time
import PIL
for f in os.listdir('.'):
    if f.endswith('.npy'):
        print('------------------------------------')
        fn, fext = os.path.splitext(f)
        print(fn)
        #time_one = time.time()
        i =code1dot6(f)
        j = PIL.Image.open(fn+'_copy.jpg')
        j.save('Centers_found_with_code_1_dot_6\{}.jpg'.format(fn))
        i.save('Centers_found_with_code_1_dot_6\{}_core_marked.png'.format(fn))
        #print(f,'Time required',round(1000*(time.time()-time_one)),'ms')
        print('------------------------------------')    