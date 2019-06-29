import numpy
import scipy
from scipy import misc
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
from glob import glob
import imageio  

#imageio.imread('big_fing.jpg')

big_fing=imageio.imread('big_fing.jpg')

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











