'''The code in this file is based on idea 2 (page 18 of notebook). The idea (hope) is that the
 core is located at the center of brightness (analogous to the center of mass, know from 
 physics)'''
 
import os
import PIL
 
def find_core_idea2(filename,n):
    import PIL
    import os
    import numpy as np
    'The line of code below, splits the filename into its name and its extention (including the .)'
    fn, fext = os.path.splitext(filename)
    'If the code is run on an npy file, the images are created in the 4 lines of code below'
    if fext == '.npy':
        img_array = np.load(filename)
        Image = PIL.Image.fromarray(img_array)
    else:
        Image = PIL.Image.open(filename)
        
    f = Image.load()

    'x-mass, is the sum of all the pixel brightnesses multiplied with the x-coordinate'
    x_mass = 0
    'y_mass, is the sum of all the pixel brightnesses multiplied with the y-coordinate'
    y_mass = 0
    'mass is the sum of all the pixel brightnesses'
    mass = 0
    
    for i in range(Image.size[0]):
        for j in range(Image.size[1]):
            x_mass = x_mass + i*(f[i,j]**n)
            y_mass = y_mass + j*(f[i,j]**n)
            mass = mass + (f[i,j]**n)
    
    #print(int(x_mass),int(y_mass,mass),int(x_mass/mass),int(y_mass/mass))
    'Below the x-coordinate and y-coordinate of the center of brightness is determined'
    x = int(x_mass/mass + 0.5)
    y = int(y_mass/mass + 0.5)
    
    print(x_mass,y_mass,mass)
    
    'The lines of code below mark the center of brightness'
    for i in range(Image.size[0]):
        Image.putpixel((i,y),(255))
    for i in range(Image.size[1]):
        Image.putpixel((x,i),(255))    
    return(Image)

'With the lines of code below, the function is performed on every image in the folder'
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = find_core_idea2(f,100)
        j = PIL.Image.open(f)
        fn, fext = os.path.splitext(f)
        j.save('Result_idea_2\{}.jpg'.format(fn))
        i.save('Result_idea_2\{}z_core_marked.jpg'.format(fn))