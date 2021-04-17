#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:07:39 2021

@author: jude
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ou = pd.read_csv("editCANES.csv")

#editN=ou[(ou.N>1)]

x=ou.F606W-ou.F814W
y=ou.F606W
plt.scatter(x,y)
plt.xlim(0,5.0)

###iscohrones############

fname="tmp1615876955.iso" # 11 gyr
fname1="tmp1615877125.iso" # 12.5 Gyr
fname2="tmp1615877141.iso" # 13 Gyr
fname3="tmp1615883590.iso" # +0.6 13.5Gyr
fname4="tmp1615883671.iso"  # +0.6 12 Gyr
fname5="tmp1616357115.iso" # +0.2  13.8Gyrs
V,I=np.genfromtxt(fname5,dtype=float,\
                    comments="#",usecols=(10,15),unpack=True)


###extinction####

dmod=19.20
E=0.02


Av=3.1*E   
Ai=1.8*E

Vfin=V+dmod+Av
Ifin=I+dmod+Ai

X=Vfin-Ifin
Y=Vfin

####fitting###
plt.plot(X,Y,color='r',label="best fit")
plt.scatter(x,y,marker="x",color='g',label="CANES")
plt.xlabel("V-I")
plt.title("CANES")
plt.ylabel("V")
plt.xlim(0,0.9)
plt.ylim(17,26)
plt.gca().invert_yaxis()
plt.legend()

D=(dmod+5)/5
D= 10 ** D
print("############ output###########")
print("Distance is: \n",D,"Pc")
print("Redding is :\n",E)
print("AGE is : \n13.8 Gyr")


fname="PAL2.XYVI.txt"
fname1="tmp1615876955.iso"





plt.show()
