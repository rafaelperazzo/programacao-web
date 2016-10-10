# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))

i=1
contador=0
while (i>0):
ai = a*i
    print ('%d'%ai)
    contador = contador + 1
   
bi = b*i
    print ('%d'%bi)
    contador = contador + 1
   
    if ai == bi:
        print ('%d'%ai)
    contador= contador + 1
    
    if contador==6:
        break
    i = i + 1
        
    
        