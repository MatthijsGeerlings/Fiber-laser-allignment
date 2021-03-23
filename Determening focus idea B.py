#Idea B, determening 'focus' met sobel operator.

#Imports
import numpy as np
import os
from numba import njit
import time
import matplotlib.pyplot as plt

#Below the folder is defined and the file path to the folder is created.
#Folder (date)
folder = 'Same image different blur'

#File path to this code
path = __file__

#Seperator in file path
seperator = os.path.sep

#List of path
list_of_path = path.split(seperator)
list_of_path.remove(list_of_path[-1])

#Creating the path to the folder
path_to_folder = list_of_path[0] + seperator
list_of_path.remove(list_of_path[0])

for i in list_of_path:
    path_to_folder = path_to_folder+i+seperator
path_to_folder = path_to_folder+folder

#Below a new folder is created where the images can be saved
image_folder = path_to_folder + seperator + 'Images'
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

#Below a new folder is created where the images can be saved
image_folder = path_to_folder + seperator + 'Images'
if not os.path.exists(image_folder):
    os.makedirs(image_folder)
   
    
@njit()
def proxy_of_focus_idea_B(array):#, power = 2):
    #This function assigns a value to the focus of a image.
    
    #Squared sobel is the sum of all squared value obtained by performing the sobel operator
    squared_sobel_vertical = 0
    squared_sobel_horizontal = 0
    
    
    for i in range(1, len(array)-1):
        for j in range(1,len(array[0])-1):
            squared_sobel_vertical = squared_sobel_vertical + (-1*array[i-1,j-1]-2*array[i-1,j]\
                                    -1*array[i-1,j+1]+array[i+1,j-1]+2*array[i+1,j]+array[i+1,j+1])**2
            
            squared_sobel_horizontal = squared_sobel_horizontal + (-1*array[i-1,j-1]-2*array[i,j-1]\
                                    -1*array[i+1,j-1]+array[i-1,j+1]+2*array[i,j+1]+array[i+1,j+1])**2
    
    root_of_squared_sum = (squared_sobel_vertical+squared_sobel_horizontal)**0.1            
    
    return root_of_squared_sum#sobel_sum # normalized_sobel_sum

    
values = []

for f in os.listdir(path_to_folder):
    if f.endswith('.npy'):
        time_one = time.time()
        print('------------------------------------')
        fn, fext = os.path.splitext(f)
        print(fn)
        array = np.load(path_to_folder+seperator+f)
        proxy = proxy_of_focus_idea_B(array)
        print(proxy)
        values.append(proxy)
        #Image = PIL.Image.fromarray(np.load(path_to_folder+seperator+f)).\
        #   save(image_folder+seperator+fn+'.jpg')
        print(round(1000*(time.time()-time_one)),'ms')
        
plt.figure(1)
#plt.yscale('log')
plt.grid()
plt.ylabel('Value')
plt.plot(values)

for i in range(1,len(values)):
    if values[i] > values[i-1]:
        print(i)