'Test file for implementation software'
''''In this function the 'multiply_array' is created'''
def creating_multiply_array_2(width, height, power = 4):
    '''This function is based on the function 'creating_multiply_array'. Differecnde is, that this 
    function produces symmetric multiply_array's, where the function creating_multiply_array
    creates assymetric multiply arrays. The power is set on 4 by default, although values of 2, 3 
    and 5 yield the same result (8 out of 10 cores found (original arrays/images))
    
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
   
    '''From multiply_array_one the multiply_array is created. This array is symetric across
    all axis, has high values (approachin 1) in the middle an low values (approachin 0) towards 
    the edges'''
    multiply_array = multiply_array_one*flip(multiply_array_one ,1)*\
        rot90(rot90(multiply_array_one))*flip( rot90(rot90(multiply_array_one)),1)
    
    '''Below the multiply_array is raised to  a power (see function input), to increase the relative 
    difference between the high and low values '''
    multiply_array = multiply_array**power
    return multiply_array