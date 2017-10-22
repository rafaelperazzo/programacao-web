# -*- coding: utf-8 -*-
import math
v=[0,0,0,0]
teste=False
if v[1]>v[2]:
    teste=not(teste)
if v[2]>v[1] and v[1]<v[2]:
    teste=not(teste)
    if v[1]>v[2]:
    teste=not(teste)
    
    
    