#Idea D page 96 notebook
import numpy as np
import os
import time
import matplotlib.pyplot as plt
from numba import njit

@njit()
def idea_d(array):
    mu_array = np.mean(array)
    focus_value = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            focus_value = focus_value + abs(array[i][j] - mu_array)
            
    return focus_value


#Below the folder is defined and the file path to the folder is created.
#Folder (date)
folder = '2021-04-01 fiber 1 close to core\\Croped arrays'

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

values = []
fns = []

for f in os.listdir(path_to_folder):
    if f.endswith('.npy'):
        print('------------------------------------')
        time_one = time.time()
        fn, fext = os.path.splitext(f)
        print(fn)
        array = np.load(path_to_folder+seperator+f)
        values.append(idea_d(array))
        print(round(1000*(time.time()-time_one)),'ms')
        fns.append(fn)
        
plt.figure(1)
plt.plot(values)
plt.grid()
plt.xlabel('File index')
plt.ylabel('Focus value')
plt.show()

print('The best focus is at:', fns[values.index(max(values))])

for i in range(1,len(values)):
   if values[i] > values[i-1] and values[i] > values[i+1]:
       print('Local maxima',i)