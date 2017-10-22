# -*- coding: utf-8 -*-
import math
v=[0,0,0,0]
for i in range (0, 3):
    v[i]=int(input('Valor %d: ' % i))
teste=False
if v[0]>v[1]:
    teste=not(teste)
if v[1]>v[2] and v[1]>v[0]:
    teste=not(teste)
if v[2]>v[1] and v[2]>v[3]:
    teste=not(teste)
if v[3]>v[2]:
    teste=not(teste)

if teste:
    print('S')
else:
    print('N')
    
    
    