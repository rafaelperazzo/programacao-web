# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de pontos: ')

for i in range (0,n,1):
    x=input('Digite o valor da coordenada X: ')
    y=input('Digite o valor da coordenada Y: ')
    
    if x>=0 and y>=0 and ((x**2)+(y**2))<=1:
        print ('SIM')
    else:
        print ('NÃO')
        