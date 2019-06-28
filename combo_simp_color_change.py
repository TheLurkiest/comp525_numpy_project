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
a1 = io.imread('venusaur.png')

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

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#print('ok this should display a CLEAN, UNALTERED IMAGE NOW as well: ')

#a1 = io.imread('2019-03-04-042807_4.jpg')
#a1 = io.imread('fing111.jpg')

#p_reply=input('enter a number representing how much greater the the color you are searching for should be in proportion to the other two in the rgb color spectrum to be above the threshhold needed to cause our code to highlight it in the resulting image-- if unsure, the best default values for most images range from around 0 to 25: ')

#color_prop_buffer=int(p_reply)

print('for our purposes, rgb color choices are represented by 0, 1 and 2, respectively, representing their specific index.  For example, to select RED as an answer to one of these prompts therefore, you must enter 0 instead.  The prompts and printed statements will also refer to RED as 0 when asking the user questions.')

print('we now ask questions pertaining to how much greater the color you wish to highlight is compared to each of the other two.  Choosing numbers between 0 and 25 is a good rule of thumb if unsure.  However, often you may find that choosing numbers here closer to 40 or 50 may be ideal.')

p_reply=input('enter how much greater you want the color you are searching for to be compared to the color in index '+ str(color_b) + ' within rgb.  ')
color_prop_buffer_b=int(p_reply)

p_reply=input('enter how much greater you want the color you are searching for to be compared to the color in index ' + str(color_c) + ' within rgb.  ')
color_prop_buffer_c=int(p_reply)


print('...now for the altered image: ')

print('testing out the X attempt now...')

boo_thresh_high = a1[:,:,color_highlighted] > a1[:,:,color_b] + color_prop_buffer_b
boo_thresh_high_g = a1[:,:,color_highlighted] > a1[:,:,color_c] + color_prop_buffer_c

booling2=boo_thresh_high & boo_thresh_high_g

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



# now to make things RED:

print('now to make our image have the portioned that were analyzed as being greater than the threshhold buffer value chosen in proportion to the other colors in the rgb spectrum not chosen have be HIGHLIGHTED BRIGHT RED to see these segments more clearly against the background:')

rgb_swap_pic[:,:,0][booling2] = 255

rgb_swap_pic[:,:,1][booling2] = 125

rgb_swap_pic[:,:,2][booling2] = 125

plt.imshow(rgb_swap_pic)
plt.show()

imsave('red_alt.png', rgb_swap_pic)




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




im=rgb_swap_pic

im = ndimage.gaussian_filter(im, 8)

rgb_swap_pic = rgb_swap_pic.astype('int32')
dx = ndimage.sobel(im, 0)  # horizontal derivative
dy = ndimage.sobel(im, 1)  # vertical derivative
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
scipy.misc.imsave('sobel_alt.png', mag)



im=rgb_swap_pic
im = ndimage.gaussian_filter(im, 8)
sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)

plt.imshow(im)

imsave('sobel_alt2.png', im)


#------------------------------------------------------------------------

plt.imshow(im)
plt.show()


#im = ndimage.rotate(im, 15, mode='constant')
#im = ndimage.gaussian_filter(im, 8)

#im = ndimage.rotate(im, 15, mode='constant')
im = ndimage.gaussian_filter(im, 8)


sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)

plt.imshow(im)

plt.show()
plt.imshow(sx)

plt.show()
plt.imshow(sy)

plt.show()
plt.imshow(sob)

plt.show()




#------------------------------------------------------------------------


im=imageio.imread('2019-03-04-042807_5.jpg')


plt.imshow(im)
plt.show()


im = ndimage.rotate(im, 15, mode='constant')
im = ndimage.gaussian_filter(im, 8)


im = ndimage.rotate(im, 15, mode='constant')
im = ndimage.gaussian_filter(im, 8)


sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)

plt.imshow(im)

plt.show()
plt.imshow(sx)

plt.show()
plt.imshow(sy)

plt.show()
plt.imshow(sob)

plt.show()


# ===============================================================







