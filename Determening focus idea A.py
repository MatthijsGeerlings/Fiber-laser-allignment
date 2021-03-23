#The objective here is to develop an algorithm that is capable of assigning a number to the 
#quality of 'focus'. This idea is based on A (page 80). In this idea it is assumed/hoped that the
#quality of focus can be derived from the positions of the n brightest pixels. It is assumed/hoped
#that the bright pixels will be closer together in a propperly focused image.

#Imports
import numpy as np
import os
import PIL
import cv2
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

#Function to assign a number to the 'focus' of the image (imports are numpy arrays)
def proxy_of_focus_idea_A(npy_file,n_value = 0.01):
     #value of 0.01 seems to be best for now
     array = np.load(npy_file)
    
     #Determination of the threshold value
     threshold = round(np.percentile(array,(100-(100*n_value)),interpolation='nearest'))

     #Below a binary array is created, pixels above the threshold get assigned the value 1 and 
     #pixels below the threshold get assigned the value 0'''
     np_array_binary = np.where(array>threshold,1,0)
 
     #Determination of the bright pixel locations'
     global bright_pixel_locations
     bright_pixel_locations = np.where(np_array_binary == 1)

     #List containing the bright pixel coordinates'
     global x_coords
     global y_coords
     x_coords = []
     y_coords = []

     #Filling the list of bright pixel coordinates'
     for i in range(0,len(bright_pixel_locations[0])):
         x_coords.append(bright_pixel_locations[0][i])
         y_coords.append(bright_pixel_locations[1][i])
     
     #r_pool is the distance of a pixel from the top left corner of an arrey
     r_pool = []   
     for i in range(len(x_coords)):
         r_pool.append((x_coords[i]**2+y_coords[i]**2)**0.5)     
     proxy = np.std(r_pool)
     
     proxy_x = np.std(x_coords)
     proxy_y = np.std(y_coords)
     return proxy,proxy_x,proxy_y
 

values = []
x_values = []
y_values = []

for f in os.listdir(path_to_folder):
    if f.endswith('.npy'):
        print('------------------------------------')
        fn, fext = os.path.splitext(f)
        print(fn)
        time_one = time.time()
        proxy, proxy_x, proxy_y = proxy_of_focus_idea_A(path_to_folder+seperator+f)
        print('Time required:',round(1000*(time.time()-time_one)),'ms')
        values.append(proxy)
        x_values.append(proxy_x)
        y_values.append(proxy_y)
        print(proxy)
        #Image = PIL.Image.fromarray(np.load(path_to_folder+seperator+f)).\
         #   save(image_folder+seperator+fn+'.jpg')
  
plt.figure(1)
plt.grid()
#plt.yscale('log')
plt.plot(values, color = 'blue')
plt.plot(x_values, color = 'green')
plt.plot(y_values,color = 'orange')

for i in range(1,len(values)):
    if values[i] > values[i-1]:
        print(i)