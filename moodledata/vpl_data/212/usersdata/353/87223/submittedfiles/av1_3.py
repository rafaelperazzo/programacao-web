# -*- coding: utf-8 -*-
import math
x=int(input('Valor 1:'))
y=int(input('Valor 2:'))
z=int(input('Valor 3:'))

if x>y>z:
    m=z
elif x>z>y:
    m=y
else:
    m=x 

while True:
    if m%x==0 and m%y==0 and m%z==0 :
        print (m)
        break 
    else:
        m=m+1