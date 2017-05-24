# -*- coding: utf-8 -*-
import math
n1=int(input('n1:' ))
n2=int(input('n2:' ))
n3=int(input('n3:' ))
d=1
mmc=0
while d>0:
    if (d%n1)==0 and (d%n2)==0 and (d%n3)==0:
        mmc=mmc+d
        break
    else:
        d=d+1
print(mmc)
        