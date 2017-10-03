# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI

a=int(input('Digite o valor desejado: '))

if a>=20:
    b=a//20
    c=(a-(b*20))
    if c>=10:
        d=c//10
        e=(c-(d*10))
        if e>=5:
            f=e//5
            g=(e-(f*5))
            h=(g//2)
            i=(g-(h*2))
            print('%d notas de 20' %b)
            print('%d notas de 10' %d)
            print('%d notas de 5' %f)
            print('%d notas de 2' %h)
            print('%d notas de 1' %i)
       

            
        
   
   
   
   
  