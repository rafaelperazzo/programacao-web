# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('digite a quantidade de vezes:')
i=1

while i<=n:
    x= input('Digite a coordenada x:')
    y= input('Digite a coordenada y:')
    if x>=0 and y>=0 and ((x**2)+(y**2))>=1:
        print ('SIM')
    else:
        print ('NAO')
    i=i+1 
    
