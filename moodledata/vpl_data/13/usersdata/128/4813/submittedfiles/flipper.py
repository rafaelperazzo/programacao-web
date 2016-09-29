# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

p=input('Posição de P: ')
r=input('Posição de R: ')

if p==0:
    print ('C')
    
elif p==1:
    if r==0:
        print ('B')
    elif r==1:
        print ('A')