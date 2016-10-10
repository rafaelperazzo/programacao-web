# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))

i=1
contador=0
while (i>0):
    ad = a*i
    bd = b*i
    
    
    if ad!=bd:
        print ('%d'%ad)
        contador= contador + 1
        print ('%d'%bd)
        contador= contador + 1
    if ad == bd:
        print ('%d'%ad)
        contador= contador + 1
    if contador==6:
        break
    i = i + 1
        
    
        