# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a=int(input('digite um valor a ser sacado:'))
if a>20:
    b=a//20
    print('a quantidade das notas de vinte é:%d' %b)
    if a%20!=0 and a%20>=10:
        c=(a%20)//10
        print('a quantidade das notas de dez é:%d' %c)
        elif a%20!=0 and a%20<10:
            d=(a%20)//5
            print('a quantidade das notas de cinco é:%d' %d)
            
            
        
    
    