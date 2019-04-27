import numpy as np 
from skimage import io
import matplotlib.pyplot as plt
a1=io.imread('ancient_maya.jpg')


d1={}

# create empty list

l_trunc=[]
for row in a1:               
    l_trunc.append(list(row))



for l_t_bit in l_trunc:
    for row in l_t_bit:
            try:
                    d1[tuple(row)]=d1[tuple(row)]+1
            except:
                    d1[tuple(row)]=1

#=========================================================================


def key_sorter(l_in):
    return l_in[1]

l_midstep2 = []
l_midstep2 = list(d1.items())

l_midstep2.sort(key=key_sorter)

l_output = []

for l_step in l_midstep2:
    l_output.append(l_step[0])


l_output.reverse()



#=========================================================================
p_reply=''
p_reply=input('break here to quit')
#=========================================================================

l_sorted2=[]

new_color=True

safety_valve_debug_counter=0

for l_o_bit in l_output:
	# breaks for debugging to avoid crazy loop errors if mistakes happen here now
	# while under testing:
	if(len(l_sorted2)>=10):
		print('break here to debug')
		break
	if(safety_valve_debug_counter<=80):
		safety_valve_debug_counter=safety_valve_debug_counter+1
	else:
		print('break here to debug')
		break
	# debugs concluded!

	if(len(l_sorted2)==0):
		l_sorted2.append(l_o_bit)
	else:
		for l_s_bit in l_sorted2:
			if(abs(l_o_bit[0] - l_s_bit[0]) <= 5):
				if(abs(l_o_bit[1] - l_s_bit[1]) <= 5)
					if(abs(l_o_bit[2] - l_s_bit[2]) <= 5):
						new_color=False
		if(new_color==True):
			l_sorted2.append(l_o_bit)
			d1[l_o_bit] = d1[l_o_bit] + d1[l_s_bit]
			del d1[l_s_bit]
		else:
			new_color=True









