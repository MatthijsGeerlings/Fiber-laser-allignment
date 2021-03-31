import numpy as np
import pathlib
import cv2
import PIL
import time

def import_or_create_and_save_multiply_array_version_3(width,height,mu_x = -1,\
                                                       mu_y = -1, sigma_x = -1, sigma_y = -1, C = 50 ):    
    '''In this function the multiply array is saved in a folder in the home path. The multiply array
    is created with a gausian function, so the center (of highest values) can be easily modified.
    All the ellements in the multiply array are integers.'''
    
    if mu_x == -1:
        mu_x = width/2
    
    if sigma_x == -1:
        sigma_x = min(width,height)/5
    
    if mu_y == -1:
        mu_y = height/2
    
    if sigma_y == -1:
        sigma_y = min(width,height)/5
    
    
    #home_path is the path to the home folder
    home_path = pathlib.Path.home()
    
    #config_path is the path to the folder containing the multply array
    config_path = home_path.joinpath('multpiply arrays')
    
    #If the config path is non existing, it is created
    if not config_path.exists():
        config_path.mkdir(parents=True)
    
    file_path = config_path.joinpath('multpiply_array_'+'width_'+str(width)+'_'+'height_'\
                    +str(height)+'_x_center_'+str(mu_x)+'_y_center_'+str(mu_y)+\
                    '_standard_deviation_x_'+str(sigma_x)+'_standard_deviation_y_'+str(sigma_y)+\
                    '_C_'+str(C)+'.npy')

    
    #Trying if file exists with file_path
    try:
        # For now multiply_array is global (this will be changed later)
        print('Try if the multiply array file exists in: ',file_path)
        multiply_array = np.load(file_path)
        print('File is existing in the folder')
    except IOError:
        #If the file does not exist in the folder, the multiply array is created and saved in the 
        #folder
        print("File non existing in folder")
        print('Creating multiply array with dimensions:',[width,height])
        
        zeros = np.zeros((100,100))

        #redifiening mu and sigma for x and y to fit in the 100 by 100 array
        mu_x = mu_x*100/width
        mu_y = mu_y*100/height
        sigma_x = sigma_x*100/width
        sigma_y = sigma_y*100/height
        
        e = 2.718281828
        A = 255-C
        
        for i in range(100):
            for j in range(100):
                zeros[i][j] = int((A*e**-(((j-mu_x)/(sigma_x))**2)*A*e**-(((i-mu_y)/(sigma_y))**2\
                                                                          ))**0.5+C)
                
        multiply_array = zeros
    

        multiply_array = cv2.resize(multiply_array,(width,height)).astype('int8')
        
        #PIL.Image.fromarray(multiply_array).show()
        print('Save multiply array')
        np.save(file_path,multiply_array)
    return multiply_array

time_one = time.time()
array = import_or_create_and_save_multiply_array_version_3(960, 1280)
print('dtype',array.dtype)
print('Time elapsed',round(1000*(time.time()-time_one)),'ms')

PIL.Image.fromarray(np.array(array)).show()