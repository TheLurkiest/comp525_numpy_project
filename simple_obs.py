import numpy as np

from PIL import Image
from pytesseract import image_to_string

# test1.jpg
# color_coded_topo_with_legends.jpg

print(str(image_to_string(Image.open('test1.jpg'))))
# print(image_to_string(Image.open('test1.jpg'), lang='eng'))

s1=str(image_to_string(Image.open('test1.jpg')))
l1=s1.split('\n')

l2 = []

for l1_bit in l1:
    if(len(l1_bit)>0):
        l2.append(l1_bit)

# now without empty quotes hopefully

print(str(l2))

l3=[]

for l2_bit in l2:
    if(l2_bit.isalpha()==False):
        l3.append(l2_bit)

# now without letters
print(str(l3))

s1=' '.join(l3)

l4=[]

l4=s1.split(' ')

len1=list(range(len(l4)))

print(str(len1))
print(str(l4))

last_val=int(l4[0])

looped1=False




for len_bit in len1:
    # print(str(len_bit))
    print(str(l4[len_bit]))
    if((looped1==True) and (int(l4[last_val]<int(l4[len_bit])))==True ):
        print('stuff happens')
        del l4[len_bit]
    if((int(last_val)+1) < int(len(len1)):
        last_val=last_val+1
    looped1=True
print(l4)
