''''In this function the 'multiply_array' is created'''
def creating_multiply_array(width, height, power = 5):
    '''This function creates the multiply array which is used to find the fiber core. The inputs are
    the width and height of the image (in pixels), depending on the camere used. The power 
    determines the relative difference in the values between the middle and the edges of the 
    multiply_array. power is set to 5 by default.'''
    
    'Required imports'
    from numpy import linspace, rot90

    '''Below multiply_array_one is created this is an array with the same dimensions as the 
    'image'. This array has high values (approaching 1) towards the vertical middle and low values
    (approaching 0) towards the bottom and top 
    '''
    multiply_array_one = (linspace(2,0,width*height).reshape(height,width)*\
        linspace(0,2,width*height).reshape(height,width))

    '''Below multiply_array_two is created, this is an array with the same dimensions as the 
    'image' rotated by 90 degrees. This array also has high values (approachin 1) towards the 
    vertical middle and low values (approaching 0) towards the upper and lower edge'''
    multiply_array_two = (linspace(2,0,width*height).reshape(width,height)*\
        linspace(0,2,width*height).reshape(width,height))
    
    '''Below multiply_array_two is rotated by 90 degrees. The new array (multiply_array_rot) has 
    the same dimensions as the 'image', and has high values towards the horizontal middle 
    (approaching 1) and low values towards the horizontal (left and right) edges (approaching 0) '''
    multiply_array_two_rot = rot90(multiply_array_two)

    '''Below multiply_array_one en multiply_array_two_rot are multiplied to create an array with
    high (approaching 1) values towards both the horizontal and vertical middle, and low 
    (approaching 0) values towards all edges'''
    multiply_array = multiply_array_one*multiply_array_two_rot
    
    '''Below the multiply_array is raised to  a power (see function input), to increase the relative 
    difference between the high and low values '''
    multiply_array = multiply_array**power
    return multiply_array