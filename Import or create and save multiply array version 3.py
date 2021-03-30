import numpy as np
import pathlib
import cv2
import PIL
import time

def import_or_create_and_save_multiply_array_version_3(width,height,mu_x = -1,\
                                                       mu_y = -1, sigma_x = -1, sigma_y = -1, A = 255 ):    
    '''In this function the multiply array is saved in a folder in the home path. The multiply array
    is created with a gausian function, so the center (of highest values) can be easily modified.
    All the ellements of the multiply array are integers.'''
    
    # mu_x value of the gausian function is defined in the middle, if no value is provided as an
    #input
    if mu_x == -1:
        mu_x = int(width/2)
        
    # mu_y value of the gausian function is defined in the middle, if no value is provided as an
    #input
    if mu_y == -1:
        mu_y = int(height/2)
    
    #If no value for sigma_x is entered, it is defined as 1 fifth of the width
    if sigma_x == -1:
        sigma_x = width/5
    
    #If no value for sigma_y is entered, it is defined as 1 fifth of the height
    if sigma_y == -1:
        sigma_y = height/5
    
    
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
                    '_Amplitude_'+str(A)+'.npy')

    
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
        
        
        #Two temporary lines of code
        global gauss_x
        global gauss_y
        
        
        #Creating x gaussian
        
        #Determening x_devider
        dividers = [width]
        results = [abs(width-100)]
        for i in range(1,int(width/2)):
            if width%i == 0:
                dividers.append(i)
                results.append(int(abs(100-width/i)))
        x_divider = dividers[results.index(min(results))]      
        
        # Redefining mu_x and sigma_x
        mu_x = mu_x/x_divider
        sigma_x = sigma_x/x_divider
        
        #Defining x_range (size of the x gaussian)
        x_range = range(int(width/x_divider))
        
        # List containing the values of the gausian in the x direction
        gauss_x = []
        
        for i in x_range:
            gauss_x.append(int(A*2.718281828**(-((i-mu_x)**2/(sigma_x)**2))))
        
        #Converting gauss_x into a numpy array
        gauss_x = np.array(gauss_x)
        
        
        #Creating y gaussian
        
        #Determening y devider
        dividers = [height]
        results = [abs(height-100)]
        for i in range(1,int(height/2)):
            if height%i == 0:
                dividers.append(i)
                results.append(int(abs(100-width/i)))
        y_divider = dividers[results.index(min(results))]        
        
        # Redefining mu_y and sigma_y
        mu_y = mu_y/y_divider
        sigma_y = sigma_y/y_divider
        
        #Defining y_range (size of the y gaussian)
        y_range = range(int(height/y_divider))
        
        # List containing the values of the gausian in the y direction
        gauss_y = []
        
        for i in y_range:
            gauss_y.append(int(A*2.718281828**(-((i-mu_y)**2/(sigma_y)**2))))
        
        #Converting gauss_y into a numpy array
        gauss_y = np.array(gauss_y)
    
        multiply_array = (np.dot(gauss_x[:,None],gauss_y[None,:]))**0.5
        multiply_array = cv2.resize(multiply_array,(width,height))
        
        multiply_array = multiply_array.astype('int16')
    
        print('Save multiply array')
        np.save(file_path,multiply_array)

    return multiply_array

time_one = time.time()
array = import_or_create_and_save_multiply_array_version_3(960, 1280,600,500,96,128)
print('Time elapsed',round(1000*(time.time()-time_one)),'ms')

PIL.Image.fromarray(np.array(array)).show()