import numpy as np
from skimage import io
import imageio
import matplotlib.pyplot as plt

# ===========================================

import numpy
import scipy
from scipy import misc
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
from glob import glob

# ===========================================

from scipy.misc import imsave

# ===========================================

#fing111.jpg
#a1 = io.imread('2019-03-04-042807_4.jpg')
#a1 = io.imread('fing111.jpg')
#a1 = io.imread('venusaur.png')
a1 = io.imread('ivysaur.png')

plt.imshow(a1)
plt.show()

# this makes our image array coarser and therefore, quicker to perform changes to-- comment/uncomment this statement below to make things quicker or more detailed/slower-- or increase/decrease the numbers ::5, ::5 to fine-tune this feature:
#a1=a1[::5,::5]

p_reply = -1

p_reply = input('enter 0, 1, or 2 to alter how red, green or blue the photo is, respectively: ')

p_reply=int(p_reply)

while(p_reply<0 or p_reply>2):
    p_reply = input('enter 0, 1, or 2 to alter how red, green or blue the photo is, respectively: ')
    p_reply = int(p_reply)

color_highlighted=p_reply
color_b=0
color_c=0

if(color_highlighted == 0):
    color_b=1
    color_c=2
if(color_highlighted == 1):
    color_b=0
    color_c=2
if(color_highlighted == 2):
    color_b=0
    color_c=1

color_selection=int(p_reply)
p_reply=14
#p_reply=input('the color we are searching for should be proportionally higher then '+ str(['red','green','blue'][color_b]) + ' by a value of at least this much more: ')
color_prop_buffer_b=int(p_reply)

p_reply=14
#p_reply=input('the color we are searching for should be proportionally higher then '+ str(['red','green','blue'][color_c]) + ' by a value of at least this much more: ')
color_prop_buffer_c=int(p_reply)

boo_thresh_high_b = a1[:,:,color_highlighted] > a1[:,:,color_b] + color_prop_buffer_b
boo_thresh_high_c = a1[:,:,color_highlighted] > a1[:,:,color_c] + color_prop_buffer_c

default_max_color_b=-1000
default_max_color_c=-1000

#p_reply='blue'
p_reply=input('enter "red", "green" or "blue" if you wish to assign a max threshhold values for your color search for one of those color values: ')
if(p_reply==str(['red','green','blue'][color_b])):
    p_reply=25
    #p_reply=input('enter MAX color value buffer for the color ' + str(['red','green','blue'][color_b]) + ' (suggested values= 10-80... just enter 255 if you do not want a max threshhold): ')
    default_max_color_b=int(p_reply)
    boo_thresh_high_max_b = a1[:,:,color_highlighted] < a1[:,:,color_b] + color_prop_buffer_b + default_max_color_b
    booling2=boo_thresh_high_b & boo_thresh_high_c & boo_thresh_high_max_b
elif(p_reply==str(['red','green','blue'][color_c])):
    p_reply=8
    #p_reply=input('enter MAX color value buffer for the color ' + str(['red','green','blue'][color_c]) + ' (suggested values= 10-80... just enter 255 if you do not want a max threshhold): ')
    default_max_color_c=int(p_reply)
    boo_thresh_high_max_c = a1[:,:,color_highlighted] < a1[:,:,color_c] + color_prop_buffer_c + default_max_color_c
    booling2=boo_thresh_high_b & boo_thresh_high_c & boo_thresh_high_max_c
else:
    booling2=boo_thresh_high_b & boo_thresh_high_c

anti_booling2 = ~ booling2

rgb_swap_pic=a1

rgb_swap_pic[:,:,color_highlighted][booling2] = 0
plt.imshow(rgb_swap_pic)
plt.show()

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# now to make things green:

print('now to make our image have the portioned that were analyzed as being greater than the threshhold buffer value chosen in proportion to the other colors in the rgb spectrum not chosen have be HIGHLIGHTED BRIGHT GREEN to see these segments more clearly against the background:')

rgb_swap_pic[:,:,0][booling2] = 125

rgb_swap_pic[:,:,1][booling2] = 255

rgb_swap_pic[:,:,2][booling2] = 125

plt.imshow(rgb_swap_pic)
plt.show()

imsave('green_alt.png', rgb_swap_pic)


# now to make things RED:

print('now to make our image have the portioned that were analyzed as being greater than the threshhold buffer value chosen in proportion to the other colors in the rgb spectrum not chosen have be HIGHLIGHTED BRIGHT RED to see these segments more clearly against the background:')

rgb_swap_pic[:,:,0][booling2] = 255

rgb_swap_pic[:,:,1][booling2] = 125

rgb_swap_pic[:,:,2][booling2] = 125

plt.imshow(rgb_swap_pic)
plt.show()

imsave('red_alt.png', rgb_swap_pic)


print('now to make our image have the portioned that were analyzed as being greater than the threshhold buffer value chosen in proportion to the other colors in the rgb spectrum not chosen have be HIGHLIGHTED BRIGHT BLUE to see these segments more clearly against the background:')

rgb_swap_pic[:,:,0][booling2] = 125

rgb_swap_pic[:,:,1][booling2] = 125

rgb_swap_pic[:,:,2][booling2] = 255

plt.imshow(rgb_swap_pic)
plt.show()

imsave('blue_alt.png', rgb_swap_pic)



print('now we allow you to pick how you want to highlight the selected portions of this image')

p_reply=input('from 0 to 255, how RED do you want the highlighted portions of this image to be?')
p_reply=int(p_reply)
rgb_swap_pic[:,:,0][booling2] = p_reply

p_reply=input('from 0 to 255, how GREEN do you want the highlighted portions of this image to be?')
p_reply=int(p_reply)
rgb_swap_pic[:,:,1][booling2] = p_reply

p_reply=input('from 0 to 255, how BLUE do you want the highlighted portions of this image to be?')
p_reply=int(p_reply)
rgb_swap_pic[:,:,2][booling2] = p_reply


plt.imshow(rgb_swap_pic)
plt.show()

imsave('selected_color_change.png', rgb_swap_pic)




h_only = rgb_swap_pic
try:
    h_only[:,:,3][anti_booling2] = 0
    h_only[:,:,0][anti_booling2] = 255
    h_only[:,:,1][anti_booling2] = 255    
    h_only[:,:,2][anti_booling2] = 0   
except:
    h_only[:,:,0][anti_booling2] = 255
    h_only[:,:,1][anti_booling2] = 255    
    h_only[:,:,2][anti_booling2] = 0   


plt.imshow(h_only)
plt.show()
imsave('highlighted_color_only.png', h_only)





