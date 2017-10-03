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
    
    if c<10:
        d=c//5
        e=(c-(d*5))
        f=e//2
        g=(e-(f*2))
        print('%d notas de 20' %b)
        print('0 notas de 10')
        print('%d notas de 5' %d)
        print('%d notas de 2' %f)
        print('%d notas de 1' %g)

if a<20:
    b=a//10
    c=(a-(b*10))
    if c>=5:
        d=c//5
        e=(c-(d*5))
        f=e//2
        g=(e-(f*2))
        print('0 notas de 20')
        print('%d notas de 10' %b)
        print('%d notas de 5' %d)
        print('%d notas de 2' %f)
        print('%d notas de 1' %g)
    
    
    
       

            
        
   
   
   
   
  