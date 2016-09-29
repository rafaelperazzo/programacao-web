# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('valor de a:')
b=input('valor de b:')
c=input('valor de c:')
d=input('valor de d:')
contador=0

if a>b:
    contador=contador+1
if b>c and b>a:
    contador=contador+1
if c>d and c>b and c>a:
    contador=contador+1
if d>a and d>b and d>c:
    contador=contador+1
    
if contador==1:
    print('s')

else: 
    print('n')

    
    
    
    
    
    

