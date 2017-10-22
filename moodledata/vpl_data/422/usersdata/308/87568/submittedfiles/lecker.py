# -*- coding: utf-8 -*-
import math
v=[0,0,0,0]
teste=False
if v[1]>v[2]:
    teste=not(teste)
if v[2]>v[1] and v[1]<v[2]:
    teste=not(teste)
if v[3]>v[2] and v[3]>v[4]:
    teste=not(teste)
if v[4]>v[3]:
    teste=not(teste)

if teste:
    print('S')
else
    print('N')
    
    
    