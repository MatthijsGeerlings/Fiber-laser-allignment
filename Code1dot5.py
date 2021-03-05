'Code 1.5 '
''' 'This code is in essence the same as code 1.2, in this code however, all operations are 
perforemd on NumPy arrays to increase up competational speed'''

'Below the npy_file is defined (in a function this will be an input)'
npy_file = 'fiber_end_2001001_0.npy'
'n_value (in a function this will be an input (with an default value))'
n_value = 0.001

def code1dot5(npy_file,n_value = 0.001):
    import time
    time_one = time.time()
    from numpy import percentile, where, load
    from copy import copy
    
 
    
    'Loading of npy_file'
    np_array_original = load(npy_file)

    'Bepalen threshold'
    threshold = round(percentile(np_array_original,(100-(100*n_value)),interpolation='nearest'))

    np_array_binary = where(np_array_original>threshold,1,0)

    'The lines of code below put the edges of the image to 0'
    'Puts the top column to 0'
    np_array_binary[0,:] = 0 
    'Puts the lowest column to 0'
    np_array_binary[-1,:] = 0
    'Puts the left column to zero'
    np_array_binary[:,0] = 0
    'Puts the right column to zero'
    np_array_binary[:,-1] = 0    

    bright_pixel_locations = where(np_array_binary == 1)

    'List containing the bright pixel coordinates'
    bright_coords = []

    for i in range(0,len(bright_pixel_locations[0])):
         bright_coords.append([bright_pixel_locations[0][i],bright_pixel_locations[1][i]])

    'Variable required in while loop, so the function does not hang'
    previous_length_bright_coords = -1
    
    'Here the important stuff happens'
    'Number of bright neighbors required'
    bright_negihbors_required = 4
    while len(bright_coords)>=1:
        
        'Copy of the binary array'
        binary_copy = copy(np_array_binary)
        bright_coords_copy = copy(bright_coords)
    
        'Important for loop'
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
        
        
        if previous_length_bright_coords == len(bright_coords) and len(bright_coords)>2.5:
            bright_coords.remove(bright_coords[0])
            bright_coords.remove(bright_coords[-1])
            
        if previous_length_bright_coords == len(bright_coords) and len(bright_coords)<2.5:
            print('Bright neighbors required',bright_negihbors_required)
            print(len(bright_coords))
            print('Break')
            break
        
        '''
        if previous_length_bright_coords == len(bright_coords) and previous_length_bright_coords !=0:
            print('Bright neighbors required',bright_negihbors_required)
            print(len(bright_coords))
            print('Break')
            break
        '''
        
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
    print('Time required to find core',round(1000*(time.time()-time_one)),'ms')
    return([x,y])   

'Performing the protocol on every numpy array in the map'
import os
import time
for f in os.listdir('.'):
    if f.endswith('.npy'):
        print('------------------------------------')
        time_one = time.time()
        i =code1dot5(f,0.001)
        print(i)
        print(f,'Time required',round(1000*(time.time()-time_one)),'ms')
        print('------------------------------------')    