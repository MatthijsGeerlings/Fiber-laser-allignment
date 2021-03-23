'Test stuff for focus detection'

'Required imports'
import scipy.ndimage
import numpy as np
import os
import PIL
from numba import njit
import time

#Below the folder is defined and the file path to the folder is created.
#Folder (date)
folder = '2021-03-22'

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

def var_of_laplacian(array):
    var_laplacian = scipy.ndimage.laplace(array).var()
    normalized_var_laplacian = var_laplacian/np.sum(array)
    return normalized_var_laplacian

for f in os.listdir(path_to_folder):
    if f.endswith('.npy'):
        time_one = time.time()
        print('------------------------------------')
        fn, fext = os.path.splitext(f)
        print(fn)
        array = np.load(path_to_folder+seperator+f)
        print(var_of_laplacian(array))
        Image = PIL.Image.fromarray(np.load(path_to_folder+seperator+f)).\
            save(image_folder+seperator+fn+'.jpg')
        print(round(1000*(time.time()-time_one)),'ms')