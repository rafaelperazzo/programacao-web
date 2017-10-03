# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
g = 9.81
E = 0.000002
f = input ('Digite f: ')
L = input ('Digite L: ')
Q = input ('Digite Q: ')
DeltaH = input ('Digite H: ') 
v = input ('Digite v: ')
x = (((8*f)*L)*(Q**2))
y = (((math.pi**2)*g)*DeltaH)
D = ((x / y)**(1/5))
print('D = %.4f' %D )



