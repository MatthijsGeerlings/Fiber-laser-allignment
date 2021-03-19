'Import or create and save multiply array'
'This function might not work on all operating systems'

import numpy as np
import os 

def import_or_create_and_save_multiply_array_version_2(width,height,power = 2.5):    
    '''The inputs must be the width and the height of the camera.

    This function is essentially the same as the function: 
    import_or_create_and_save_multiply_array (see description below). The most important 
    differences are: 
    -This function does not have a  function within a function (creating_multiply_array_2), 
    but does all the things that creating_multiply_array_2 does in the main code.
    -The multiply array is not stored in the GitHub folder but the folder containing the Github
    folder.

    import_or_create_and_save_multiply_array: This function checks whether the file (file_name 
    in code) containing the multiply array exists (in the same folder that contains this function). 
    If it exists and is the proper size (width and height), then the multiply array is imported and 
    used. If the file containing the multiply array does not exist (in the folder) or is the wrong 
    size, the multiply array is created (with the function:  'creating_multiply_array_2'), saved in 
    the folder (under file_name), and used.'''

    #Path is the file path to this code
    path = __file__
    

     #Nelow the seperation sine of the file path is determined (this depends on the operating
     #system). 
    seperator = os.path.sep
    
    #A list of the file path is created, the elements are split based on the seperator.
    list_of_path = path.split(seperator)

     #removing the last 5 elements
    for i in range(5):
         list_of_path.remove(list_of_path[-1])

     #Defining element '0' in list of path as the first element in the new path
    file_path = list_of_path[0]
    list_of_path.remove(list_of_path[0])

     #Creating the new path
    for i in list_of_path:
         file_path = file_path + seperator +i
    file_path = file_path + seperator + "multiply_array.npy"      


    #Trying if file exists
    try:
        # For now multiply_array is global (this will be changed later)
        print('Try if the multiply array file exists in: ',file_path)
        multiply_array = np.load(file_path)
       
    except IOError:
        #If the file does not exist in the folder, the multiply array is created and saved in the 
        #folder
        print("File non existing in folder")
        print('Creating multiply array with dimensions:',[width,height])
        #Creating the multiply array (in the same way as the function: creating_multiply_array_2)
        multiply_array_one = (np.linspace(2,0,width*height).reshape(height,width))
        multiply_array_one = multiply_array_one*np.flip(multiply_array_one ,1)*\
        np.rot90(np.rot90(multiply_array_one))*np.flip(np.rot90(np.rot90(multiply_array_one)),1)
    
        multiply_array_two = (np.linspace(2,0,width*height).reshape(width,height))
        multiply_array_two = multiply_array_two*np.flip(multiply_array_two ,1)*\
        np.rot90(np.rot90(multiply_array_two))*np.flip(np.rot90(np.rot90(multiply_array_two)),1)
                
        multiply_array = multiply_array_one * np.rot90(multiply_array_two)
    
        multiply_array = multiply_array**power
        print('Save multiply array')
        np.save(file_path,multiply_array)
    else:
        print('File existing in folder')
        if len(multiply_array[0]) != width or  len(multiply_array) != height:
            #If the multiply_array does exist but has the wrong dimensions, a multiply_array with
            #the propper dimesions is created and saved.
            print('But wrong dimensions')
            print('Create multply array with (propper) dimensions:',[width,height])
            multiply_array_one = (np.linspace(2,0,width*height).reshape(height,width))
            multiply_array_one = multiply_array_one*np.flip(multiply_array_one ,1)*\
            np.rot90(np.rot90(multiply_array_one))*np.flip(np.rot90(np.rot90(multiply_array_one)),\
                                                           1)
    
            multiply_array_two = (np.linspace(2,0,width*height).reshape(width,height))
            multiply_array_two = multiply_array_two*np.flip(multiply_array_two ,1)*\
            np.rot90(np.rot90(multiply_array_two))*np.flip(np.rot90(np.rot90(multiply_array_two)),\
                                                           1)
                
            multiply_array = multiply_array_one * np.rot90(multiply_array_two)
    
            multiply_array = multiply_array**power
            print('Save new multiply array')
            np.save(file_path,multiply_array)
        else:
            print('With the propper dimensions (',[width,height],')')
    return multiply_array

multiply_array = import_or_create_and_save_multiply_array_version_2(960, 1280)