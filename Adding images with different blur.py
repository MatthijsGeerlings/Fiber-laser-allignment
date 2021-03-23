#Adding images with different blur to the folder 'Same image different blur'

#Required imports
import cv2
import PIL
import numpy as np

path = "C:\\Users\\Matthijs\\Documents\\NH4\\Afstuderen\\Dispertech\\Focus determination\\Same image different blur\\fiber_end.jpg"

Image = cv2.imread(path)
ones = np.ones((len(Image),len(Image[0])))
for i in range(len(Image)):
    for j in range(len(Image[0])):
        ones[i,j] = Image[i,j,0]

Image = ones

Image1 = PIL.Image.fromarray(Image)

ksize = (100,100)

Image2 = PIL.Image.fromarray(cv2.blur(Image,ksize))

for i in np.arange(1,101,1):
    blured_array = cv2.blur(Image,(i,i))
    Image1 = PIL.Image.fromarray(blured_array)
    j = 'fiber_end_blur_'+str(i)
    #Image1.save('Same image different blur\{}.jpg'.format(j))
    k = 'fiber_end_blur_array_'+str(i)
    np.save('Same image different blur\{}.npy'.format(k),blured_array)