import numpy as np
from skimage import io

import matplotlib.pyplot as plt



a1 = io.imread('2019-03-04-042807_4.jpg')

# uncomment this line to make the job simpler (takes less time to make alterations/calculations, but rougher)
# make the ::5, ::5 into larger numbers to simplify/quicken this process if too slow
a1=a1[::5,::5]


king_boo = np.zeros(a1.size,dtype=np.bool)
king_boo.shape = (a1.shape[0],a1.shape[1],a1.shape[2])




p_reply = -1

p_reply = input('enter 0, 1, or 2 to alter how red, green or blue the photo is, respectively: ')

p_reply=int(p_reply)

while(p_reply<0 or p_reply>2):
    p_reply = input('enter 0, 1, or 2 to alter how red, green or blue the photo is, respectively: ')
    p_reply = int(p_reply)


color_selection=int(p_reply)

king_boo2=king_boo
king_boo[:, :, color_selection] = True


# ok here we try to create 

a2=a1
king_boo2[:, :, 1] = True

boo_thresh_high_redder = a2[:,:,0] > (((a2[:,:,1] + a2[:,:,2])/2) +20)
#booling2_r=boo_thresh_high_redder & king_boo2
booling2_r=boo_thresh_high_redder

rgb_swap_pic2=a2

#rgb_swap_pic2[booling2_r] = 0
rgb_swap_pic2[:,:,0][booling2_r] = 0


plt.imshow(rgb_swap_pic2)
plt.show()






boo_thresh_high = a1 > 125
booling2=boo_thresh_high & king_boo

rgb_swap_pic=a1

rgb_swap_pic[booling2] = 0
plt.imshow(rgb_swap_pic)
plt.show()




#========================


# ========================================================================================





import numpy as np
from skimage import io

import matplotlib.pyplot as plt

photo=io.imread('2019-03-04-042807_4.jpg')

plt.imshow(photo)
plt.show()

photo.shape
a1=photo

b1=a1<75

a1[b1]=35


plt.imshow(a1)
plt.show()


# we want to get a specific color range-- to specify further, we need to determine what the rgb for our searched
# color actually is:

# rgb range for finger is: 



# reddify specifically

print('new special reddification test running now...')

king_boo[:, :, 1] = True

boo_thresh_high = a1 > (a1[:,:,1] - a1[:,:,2])/2
booling2=boo_thresh_high & king_boo

rgb_swap_pic=a1

rgb_swap_pic[booling2] = 0
plt.imshow(rgb_swap_pic)
plt.show()














# ========================================================================================













import numpy as np
from skimage import io

import matplotlib.pyplot as plt

photo=io.imread('Mars_1024.jpg')

plt.imshow(photo)
plt.show()

photo.shape
a1=photo

b1=a1<75

a1[b1]=35


plt.imshow(a1)
plt.show()


# ========================================================================================



a2=photo
print(str(a2[1]))



plt.imshow(a2)


plt.show()
b2=a2[:,:,1]>171
a2[b2]=255
plt.imshow(a2)



plt.show()












# ========================================================================================

# ========================================================================================

# ========================================================================================

# altered version here: attempting to alter ONLY pixels the match the parameters we are looking to change

import numpy
import scipy
from scipy import misc
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
from glob import glob
import imageio  

#imageio.imread('big_fing.jpg')

big_fing=imageio.imread('2019-03-04-042807_4.jpg')

type(big_fing)

big_fing.tofile('big_fing.raw')
big_from_raw=np.fromfile('big_fing.raw', dtype=np.uint8)

plt.imshow(big_fing)



big_fing_memmap = np.memmap('big_fing.raw', dtype=np.uint8, shape=(230, 640, 3))


big_fing[0, 40]

# Slicings

# take a look at something like this:
# big_fing[125:177, 1:241]
# this is BACKWARDS from how most people like to display-- vertical coord come first, then horizontal (--and vert is highest at the bottom)
# ...that tells us what the colors are being displayed at these coordinates-- from the vertical y coordinates 125 to 177 on the left side of the map (from 1-241 on the x-coord)

big_fing[25:110] = 44


# Fancy indexing

big_fing[range(100), range(100)] = 235




from scipy.misc import bytescale

bytescale(big_fing)


#big_fing[299:345]=[21,121,277]

for idx, nail in enumerate(big_fing):
    if(big_fing[idx, 0, 0] > 50 and big_fing[idx, 0, 0] < 100 and (big_fing[idx, 0, 1])>32 and (big_fing[idx, 0, 2])>32 and (big_fing[idx, 0, 1] < 80) and (big_fing[idx, 0, 2]) < 80):
            big_fing[idx]=[21,121,277]
            print('idx is '+str(idx))





plt.imshow(big_fing)
plt.show()

# 50-111
# 32-79
#big_fing[10:13, 20:23]





# ========================================================================================

# ========================================================================================

# ========================================================================================

# default below: alters entire lines


import numpy
import scipy
from scipy import misc
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
from glob import glob
import imageio  

#imageio.imread('big_fing.jpg')

big_fing=imageio.imread('2019-03-04-042807_4.jpg')

type(big_fing)

big_fing.tofile('big_fing.raw')
big_from_raw=np.fromfile('big_fing.raw', dtype=np.uint8)

plt.imshow(big_fing)



big_fing_memmap = np.memmap('big_fing.raw', dtype=np.uint8, shape=(230, 640, 3))


big_fing[0, 40]

# Slicings

# take a look at something like this:
# big_fing[125:177, 1:241]
# this is BACKWARDS from how most people like to display-- vertical coord come first, then horizontal (--and vert is highest at the bottom)
# ...that tells us what the colors are being displayed at these coordinates-- from the vertical y coordinates 125 to 177 on the left side of the map (from 1-241 on the x-coord)

big_fing[25:110] = 44


# Fancy indexing

big_fing[range(100), range(100)] = 235




from scipy.misc import bytescale

bytescale(big_fing)


#big_fing[299:345]=[21,121,277]

for idx, nail in enumerate(big_fing):
    if(big_fing[idx, 0, 0] > 50 and big_fing[idx, 0, 0] < 100 and (big_fing[idx, 0, 1])>32 and (big_fing[idx, 0, 2])>32 and (big_fing[idx, 0, 1] < 80) and (big_fing[idx, 0, 2]) < 80):
            big_fing[idx]=[21,121,277]
            print('line number '+str(idx) + ' is turned green')





plt.imshow(big_fing)
plt.show()

# 50-111
# 32-79
#big_fing[10:13, 20:23]







