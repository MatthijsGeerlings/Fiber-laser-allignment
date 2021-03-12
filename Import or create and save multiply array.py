'Import or create and save multiply array'

def import_or_create_and_save_multiply_array(width,height):
    '''The inputs are the width and the height of the camera.

    This function checks whether the file (file_name in code) containing the multiply array exists 
    (in the same folder that contains this function). If it exists and is the proper size (width and 
    height), then the multiply array is imported and used. If the file containing the multiply array 
    does not exist (in the folder) or is the wrong size, the multiply array is created (with the 
    function:  'creating_multiply_array_2'), saved in the folder (under file_name), and used.'''
    
    'Necesarry import'
    from numpy import save, load

    '''Creating File_exist variable as a None. This variable is used to check whether the NumPy 
    array exists'''
    File_exist = None

    'Name of the file'
    file_name = 'multiply_array.npy'


    'Function that can create the multiply array if necesarry'
    def creating_multiply_array_2(width, height, power = 2.5):
        '''This function is based on the function 'creating_multiply_array' (see description below).
        Differecne is, that this function produces symmetric multiply_array's, where the function 
        creating_multiply_array creates assymetric multiply arrays. The power is set on 2.5 by default,
        although values of 2 and 3 yield the same result (2.5 is chosen because it is halfway between 
        2 and 3).
    
        creating_multiply_array: This function creates the multiply array which is used to find the fiber
        core. The inputs are the width and height of the image (in pixels), depending on the camere 
        used. The power determines the relative difference in the values between the middle and the 
        edges of the multiply_array. power is set to 5 by default.'''
    
        'Required imports'
        from numpy import linspace, rot90, flip

        '''Below multiply_array_one is created this is an array with the same dimensions as the 
        'image'. This array goes from 2 (upper left corner) to 0 (lower right corner) with equal steps 
        '''
        multiply_array_one = (linspace(2,0,width*height).reshape(height,width))

        '''Below multiply_array_one is redefined as an array with small values towards the vertical
        edges and big values towards the vertical middle (the function is symmetric in the horizontal
        direction)'''
        multiply_array_one = multiply_array_one*flip(multiply_array_one ,1)*\
        rot90(rot90(multiply_array_one))*flip(rot90(rot90(multiply_array_one)),1)
    
        multiply_array_two = (linspace(2,0,width*height).reshape(width,height))
        multiply_array_two = multiply_array_two*flip(multiply_array_two ,1)*\
        rot90(rot90(multiply_array_two))*flip(rot90(rot90(multiply_array_two)),1)
                
        '''Creating an array with big values towards the middle (aaoriachin 1) and small values 
        towards the edges (approachin 0)'''
        multiply_array = multiply_array_one * rot90(multiply_array_two)
    
        '''Below the multiply_array is raised to  a power (see function input), to increase the relative 
        difference between the high and low values '''
        multiply_array = multiply_array**power
        return multiply_array


    'Testen of file bestaat, als '
    try:
        multiply_array = load(file_name)
        print('Try if file exists')
    except IOError:
        print("File non existing in folder")
        File_exist = False
    else:
        print('File existing in folder')
        File_exist = True
    finally:
        pass
    
    'Checking whether the multiply array exist'
    if File_exist == True:
        if len(multiply_array[0]) == width and  len(multiply_array) == height:
            print('Good dimension')
        else:
            print('Wrong dimensions')
            print('Create multply array with propper dimensions')
            multiply_array  = creating_multiply_array_2(width, height)
            print('Save multiply array')
            save(file_name,multiply_array )
 
    else:
        print('Create multiply array')
        multiply_array  = creating_multiply_array_2(width, height)
        print('Save multiply array')
        save(file_name,multiply_array )
   
    return multiply_array