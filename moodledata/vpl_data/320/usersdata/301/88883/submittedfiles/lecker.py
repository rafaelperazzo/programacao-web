# -*- coding: utf-8 -*-
import math
x= int(input('digite o valor de x: '))
y= int(input('digite o valor de y: '))
z= int(input('digite o valor de z: '))
w= int(input('digite o valor de w: '))
v=0
i=1
for i in range(1,5,1):
    while x<y<z or y<z<w or x>y or w>z:
        v=v+1
if v==1:
     print('S')
 else:
     print('N')


     

