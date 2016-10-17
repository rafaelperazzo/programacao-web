# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite um valor de 0 a 9: ')
b=input('Digite um valor de 0 a 9: ')
c=input('Digite um valor de 0 a 9: ')
d=input('Digite um valor de 0 a 9: ')
if (a==c) or (b==d):
    print ('V')
elif (a==b) and (b==d):  
    print ('F')
elif (a==c) and (b==d) :
    print ('V')
elif (b==c) or (c==d):
    print ('F')
else: 
    print ('F')


