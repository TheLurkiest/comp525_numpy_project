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








