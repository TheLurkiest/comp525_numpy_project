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








a1 = io.imread('2019-03-04-042807_4.jpg')

# uncomment this line to make the job simpler (takes less time to make alterations/calculations, but rougher)
# make the ::5, ::5 into larger numbers to simplify/quicken this process if too slow
a1=a1[::5,::5]

a1_backup=a1

king_boo = np.zeros(a1.size,dtype=np.bool)
king_boo.shape = (a1.shape[0],a1.shape[1],a1.shape[2])




p_reply = -1

p_reply = input('enter 0, 1, or 2 to alter how red, green or blue the photo is, respectively: ')

p_reply=int(p_reply)

while(p_reply<0 or p_reply>2):
    p_reply = input('enter 0, 1, or 2 to alter how red, green or blue the photo is, respectively: ')
    p_reply = int(p_reply)


color_selection=int(p_reply)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

print('ok this should display a CLEAN, UNALTERED IMAGE NOW as well: ')

a1 = io.imread('2019-03-04-042807_4.jpg')

plt.imshow(a1)
plt.show()

p_reply=input('enter a number representing how much greater the the color you are searching for should be in proportion to the other two in the rgb color spectrum to be above the threshhold needed to cause our code to highlight it in the resulting image-- if unsure, the best default values for most images range from around 0 to 25: ')

color_prop_buffer=int(p_reply)

print('...now for the altered image: ')

print('testing out the X attempt now...')

boo_thresh_high = a1[:,:,0] > a1[:,:,1] + color_prop_buffer
boo_thresh_high_g = a1[:,:,0] > a1[:,:,2] + color_prop_buffer


booling2=boo_thresh_high & boo_thresh_high_g

rgb_swap_pic=a1

rgb_swap_pic[:,:,0][booling2] = 0
plt.imshow(rgb_swap_pic)
plt.show()

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





im=rgb_swap_pic


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







