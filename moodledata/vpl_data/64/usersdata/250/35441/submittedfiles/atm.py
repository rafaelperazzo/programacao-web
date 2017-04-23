# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
n=int(input('valor a sacar:'))
i=20
contador=20
while i==1:
    if (n%i==0):
        contador=contador/2
        a=n/i
        print('%d'%a)
    i=i/2    
     
    