echo testing python image modules
echo ---------------------------
echo FOR THE TIME BEING YOU MUST DEACTIVATE YOUR VIRTUAL ENVIRONMENT BEFORE EXECUTING THIS SHELL SCRIPT FOR IT TO WORK PROPERLY... unfortunately skimage requires anaconda and cv2 needs python3.7 so I guess for now I need to be out of the virtual environment to do this... if I put anaconda into a virtual environment I could probably resolve this though-- at least such that I could use this shell script in the virtual environment
echo ---------------------------






echo ---------------------------
echo OUTPUT IMAGE FILE TEST
echo ---------------------------

echo "

# remember to use python3.7 when using cv2!
# ...also i'm pretty sure that the virtual environment wont work with cv2... although--
# i'll try it and see how/if it works.

# this is what it looks like when you want to test that cv2 works:

#$ python3.7 
#Python 3.7.1 (default, Oct 22 2018, 11:21:55)  
#[GCC 8.2.0] on linux 
#Type "help", "copyright", "credits" or "license" for more information. 
#>>> import cv2   
#>>> import numpy 
#>>> cv2.__version__ 
#'4.1.0' 
#>>>  


import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

folder_now = ''
folder_now = '/home/rustyb69/Desktop/python_image_tests/final_proj_april24_packaging_up/vis_obs_main_cell/'

# grayscale test:
a1 = cv2.imread(os.path.join(folder_now,'Mars_grayscale_topo_map.jpg'))
# Mars_grayscale_topo_map
# a1 = cv2.imread(os.path.join(folder_now,'Mars_grayscale_topo_map.jpg'))
# monotonal_insta-city.jpg

# a1 = cv2.imread(os.path.join(folder_now,'relief-shading2_rivers.jpg'))

verts=[]

m1_from_pydata2 = (verts, [], [])#create mesh from data

cv2.imwrite(folder_now+'cv_test4b.png', a1[:,:])
simp_scale = 1
a2=a1[::simp_scale,::simp_scale]
# plt.imshow(a2)
# plt.show()
list_of_tuples_a2=[]
y_a2=-1
x_a2=-1

def c_tone_set_elev(test_color):
		test_color[2] = float((sum(test_color))/10)

for e_a2 in a2:
	y_a2=y_a2+1
	for e_e_a2 in e_a2:
		x_a2=x_a2+1
		c_tone_set_elev(e_e_a2)
		e_e_a2[0]=y_a2
		e_e_a2[1]=x_a2

a2_floats=a2.astype(float)

for e_a2 in a2_floats:
	for e_e_a2 in e_a2:
			list_of_tuples_a2.append(tuple(e_e_a2))

# v_maker('topo_map', [(-1.0, 1.0, 5.0), (-1.0, -1.0, 5.0)])
# v_maker('topo_map', list_of_tuples_a2)

cv2.imwrite(folder_now+'cv_test5b.png', a2[:,:])

plt.imshow(a2)
plt.show()
a1 = cv2.imread(os.path.join(folder_now,'cv_test2.png'))
a2=a1
a2_floats=a2.astype(float)
list_of_tuples_a2 = []
for e_a2 in a2_floats:
	for e_e_a2 in e_a2:
			list_of_tuples_a2.append(tuple(e_e_a2))












" > post_output_image_file_test.py

python3.7 post_output_image_file_test.py


















echo Running python image manipulation and analysis modules now through python shell script...

echo -------------------------------------------------
echo TEST 1 STARTS NOW
echo -----------------


echo "

import numpy as np

from PIL import Image
from pytesseract import image_to_string


print('this python module is all about showing how to use important image manipulation and analysis methods in python with examples displayed.')

# 1. pytesseract -----------------------------------------------------------------------------------------
print('first we test pytesseract, which allows us to read text from an image, directly: ')

# test1.jpg
# color_coded_topo_with_legends.jpg

print(str(image_to_string(Image.open('test1.jpg'))))
# print(image_to_string(Image.open('test1.jpg'), lang='eng'))

s1=str(image_to_string(Image.open('test1.jpg')))
l1=s1.split('\n')

l2 = []

for l1_bit in l1:
    if(len(l1_bit)>0):
        l2.append(l1_bit)

# now without empty quotes hopefully

print(str(l2))

l3=[]

for l2_bit in l2:
    if(l2_bit.isalpha()==False):
        l3.append(l2_bit)

# now without letters
print(str(l3))

s1=' '.join(l3)

l4=[]

l4=s1.split(' ')

len1=list( range(len(l4) ) )

print(str(len1))
print(str(l4))

last_val=int(l4[0])

looped1=False


" > tesseract_sh_test.py

python3.7 tesseract_sh_test.py




echo -------------------------------------------------
echo TEST 2 STARTS NOW 
echo -----------------

echo "

# 2. boolean arrays -----------------------------------------------------------------------------------------

import numpy as np
from skimage import io

import matplotlib.pyplot as plt

photo=io.imread('ancient_maya.jpg')

plt.imshow(photo)
plt.show()

photo.shape
a1=photo

b1=a1<75

a1[b1]=35

b1=a1>230

a1[b1]=255


plt.imshow(a1)
plt.show()


" > boolean_array_sh_test.py

python boolean_array_sh_test.py




echo -------------------------------------------------
echo TEST 3 STARTS NOW 
echo -----------------

# 3. third_test -----------------------------------------------------------------------------------------

echo "

import numpy as np
from skimage import io

import matplotlib.pyplot as plt

photo=io.imread('ancient_maya.jpg')

plt.imshow(photo)
plt.show()

photo.shape
a1=photo

a2=a1[::7,::7]

plt.imshow(a2)
plt.show()

y_a2=-1
x_a2=-1

for e_a2 in a2:
  y_a2=y_a2+1
  for e_e_a2 in e_a2:
    x_a2=x_a2+1
    e_e_a2[2]=255
    e_e_a2[0]=y_a2
    e_e_a2[1]=x_a2



plt.imshow(a2)
plt.show()


" > nested_for_test3.py


python nested_for_test3.py




echo -------------------------------------------------
echo TEST 4 STARTS NOW- reddifying
echo -----------------

# 4. 4th_test ----------------------------------------------------------------------------$


echo "



# messing with images in python and linux

#-----------------------------------------------------------------------------
# basic colors:

# values in array images are represented by a set of 3 numbers from 0-255:

# red tones: [high, medium, low]
# green tones: [medium, high, medium]
# blue tones: [low, medium, high]


# 0 is darker (all 0's are black)
# 255 is light (all 255's is white)
#-----------------------------------------------------------------------------
# simple wholesale alterations change one color or range of colors to another
# using boolean arrays to select only the range of values we're interested in
# changing-- but impacts all 3 rgb values indiscriminately:

import numpy as np 
from skimage import io
import matplotlib.pyplot as plt
a1=io.imread('lidar_color_code.jpg')


plt.imshow(a1) 
plt.show() 


a1=a1[::5,::5]


b1=a1<3
a1[b1]=0
b1=a1>252
a1[b1]=255 

plt.imshow(a1) 
plt.show() 

#-----------------------------------------------------------------------------

# specific alterations to r, g, or b in specific ways throughout image

a1 = io.imread('lidar_color_code.jpg')

a1=a1[::5,::5]


king_boo = np.zeros(a1.size,dtype=np.bool)
king_boo.shape = (a1.shape[0],a1.shape[1],a1.shape[2])


long_l_out=[]

for a1_bit in a1:
    long_l_out.append(a1_bit)
    for a1_bit_of_bit in a1_bit:
        long_l_out.append(a1_bit_of_bit)
        
        
# boo_out.write(str(a1_bit_of_bit[0])+str(a1_bit_of_bit[1])+str(a1_bit_of_bit[2])+'\n')

boo_out=open('image_array_info.txt','w')

for long_bit in long_l_out:
    boo_out.write(str(long_bit)+'\n')

boo_out.close()




# ...so now when we want to only mess with a single column
# we use colon (:) first to grab every single array inside 
# king_boo and then 0 to grab the first element of each array

# 0 impacts red-ness, 1 impacts green-ness, 2 impacts blue-ness

p_reply = -1

p_reply = input('enter 0, 1, or 2 to alter how red, green or blue the photo is, respectively: ')

p_reply=int(p_reply)

while(p_reply<0 or p_reply>2):
    p_reply = input('enter 0, 1, or 2 to alter how red, green or blue the photo is, respectively: ')
    p_reply = int(p_reply)


color_selection=int(p_reply)

king_boo[:, :, color_selection] = True

boo_thresh_high = a1 > 125
booling2=boo_thresh_high & king_boo

rgb_swap_pic=a1

rgb_swap_pic[booling2] = 0
plt.imshow(rgb_swap_pic)
plt.show()

#-------------------------------------




" > basics2_reddify.py

python basics2_reddify.py


