
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
