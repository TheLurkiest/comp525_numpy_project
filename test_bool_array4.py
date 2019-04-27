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





