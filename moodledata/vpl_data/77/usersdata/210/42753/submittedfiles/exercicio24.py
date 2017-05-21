# -*- coding: utf-8 -*-
import math
g=int(input('digite g:'))
h=int(input('digite h:'))
if g<h:
    menor=g
else:
    menor=h
for i in range(1,menor+1,1):
    if g%i==0 and h%i==0:
        mdc=i
print(mdc)






