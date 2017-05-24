# -*- coding: utf-8 -*-
import math
n1=input('n1:')
n2=input('n2:')
if n1<n2:
    menor=n1
else:
    menor=n2
for i in range(1,menor+1,1):
    if n1%i==0 and n2%i==0:
        mdc=i
print(mdc)
    
print(cont)


    