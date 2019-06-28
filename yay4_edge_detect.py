
import numpy
import scipy
from scipy import misc
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
from glob import glob





# ===========================================

# source: https://sprites.pokecheck.org/i/002.gif

import numpy as np
from skimage import io

import imageio

import matplotlib.pyplot as plt



# 002.gif

#photo=io.imread('venusaur.png')
photo = scipy.misc.imread('2019-03-04-042807_2.jpg')

im = photo


plt.imshow(photo)
plt.show()

photo.shape
a1=photo

b1=a1<200

a1[b1]=0


plt.imshow(a1)
plt.show()

im = a1

im = im.astype('int32')
dx = ndimage.sobel(im, 0)  # horizontal derivative
dy = ndimage.sobel(im, 1)  # vertical derivative
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
scipy.misc.imsave('sobel_venusaur2.png', mag)

plt.imshow(im)
plt.show()





im = scipy.misc.imread('2019-03-04-042807_3.jpg')
im = im.astype('int32')
dx = ndimage.sobel(im, 0)  # horizontal derivative
dy = ndimage.sobel(im, 1)  # vertical derivative
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
scipy.misc.imsave('sobel_venusaur3.png', mag)

plt.imshow(im)
plt.show()


sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)

plt.imshow(sob)
plt.show()






im = scipy.misc.imread('2019-03-04-042807_4.jpg')
im = im.astype('int32')
dx = ndimage.sobel(im, 0)  # horizontal derivative
dy = ndimage.sobel(im, 1)  # vertical derivative
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)

sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)




plt.imshow(sob)
plt.show()





im=photo

im = ndimage.gaussian_filter(im, 3)

plt.imshow(im)
plt.show()

sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)


plt.imshow(sob)
plt.show()





# ===========================================


# source: # https://img.pokemondb.net/sprites/x-y/normal/bulbasaur.png




from skimage import io
import imageio

im=imageio.imread('2019-03-04-042807_5.jpg')


plt.imshow(im)
plt.show()


im = ndimage.rotate(im, 15, mode='constant')
#im = ndimage.gaussian_filter(im, 8)


im = ndimage.rotate(im, 15, mode='constant')
#im = ndimage.gaussian_filter(im, 8)


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







p_reply=''
p_reply='break in the code to exit, if desired.'





# ===========================================



# source: https://img.pokemondb.net/sprites/x-y/normal/ivysaur.png


from skimage import io
import imageio

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







p_reply=''
p_reply='break in the code to exit, if desired.'










# ===========================================


from skimage import io
import imageio


im=imageio.imread('2019-03-04-042807_3.jpg')
#im=np.fromfile('fing333.jpg')




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







# ===========================================



im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1


plt.imshow(im)

plt.show()


im = ndimage.rotate(im, 15, mode='constant')
im = ndimage.gaussian_filter(im, 8)
im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1

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





# ===========================================





im=imageio.imread('2019-03-04-042807_4.jpg')


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










