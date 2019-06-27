# approximate python code instructions (with some additions)
# ...mostly from http://scipy-lectures.org/advanced/image_processing/

import numpy
import scipy
from scipy import misc
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
from glob import glob


face=misc.face()
misc.imsave('pace.png',face)
face=misc.imread('face.png')
type(face)
face.shape, face.dtype
face.tofile('face.raw') 

face_from_raw=np.fromfile('face.raw',dtype=np.uint8)

plt.imshow(face)
# use plt.show command to show image-- commented out for now cuz i think it interrupts things:
#plt.show()# uncomment to show image 
face_from_raw=np.fromfile('face.raw',dtype=np.uint8)
face_from_raw.shape
face_from_raw.shape = (768, 1024, 3)
face_memmap = np.memmap('face.raw', dtype=np.uint8, shape=(768, 1024, 3))

for i in range(10):
    im = np.random.randint(0, 256, 10000).reshape((100, 100))
    misc.imsave('random_%02d.png' % i, im)

filelist=glob('random*.png')
filelist.sort()


f=misc.face(gray=True)
import matplotlib.pyplot as plt
plt.imshow(f,cmap=plt.cm.gray)

#plt.show()# uncomment to show image
plt.contour(f,[50,200])

#plt.show()# uncomment to show image



plt.imshow(f, cmap=plt.cm.gray, vmin=30, vmax=200) 

#plt.show()# uncomment to show image
plt.axis('off')

#plt.show()# uncomment to show image     
plt.contour(f,[50,200])

#plt.show()# uncomment to show image
plt.imshow(f[320:340,510:530],cmap=plt.cm.gray,interpolation='bilinear')

#plt.show()# uncomment to show image
plt.contour(f,[50,200])



#plt.show()# uncomment to show image



plt.imshow(f[320:340,510:530],cmap=plt.cm.gray,interpolation='bilinear')                    

#plt.show()# uncomment to show image


plt.imshow(f[320:340,510:530],cmap=plt.cm.gray,interpolation='bilinear')                    

plt.imshow(f[320:340,510:530],cmap=plt.cm.gray,interpolation='nearest')













face = misc.face(gray=True)

face[0, 40]

# Slicing

face[10:13, 20:23]


face[100:120] = 255

lx, ly = face.shape

X, Y = np.ogrid[0:lx, 0:ly]

mask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 > lx * ly / 4


# Masks

face[mask] = 0

# Fancy indexing

face[range(400), range(400)] = 255

plt.imshow(face)
plt.show()# uncomment to show image












