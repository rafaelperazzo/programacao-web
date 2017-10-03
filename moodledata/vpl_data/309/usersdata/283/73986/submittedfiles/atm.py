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
            print('b')
            print('d')
            print('f')
            print('h')
            print('i')
    
    if c<10:
        d=c//5
        e=(c-(d*5))
        f=e//2
        g=(e-(f*2))
        print(b)
        print(0)
        print(d)
        print(f)
        print(g)

if a<20:
    b=a//10
    c=(a-(b*10))
    if c>=5:
        d=c//5
        e=(c-(d*5))
        f=e//2
        g=(e-(f*2))
        print('0')
        print(b)
        print(d)
        print(f)
        print(g)
    if c<5:
        d=c//2
        e=(c-(d*2))
        print('0')
        print(b)
        print('0')
        print(d)
        print(e)
    
    
    
       

            
        
   
   
   
   
  