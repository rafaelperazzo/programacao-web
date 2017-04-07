# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CODIGO AQUI
a=int(input('digite um valor para o saque:'))
if a>20:
    b=a//20
    print('a quantidade das notas de vinte é:%d' %b)
    if (a%20)!=0 and (a%20)>=10:
        c=(a%20)//10
        print('a quantidade das notas de dez é:%d' %c)
        elif a%20!=0 and (a%20)<10:
            d=(a%20)//5
            print('a quantidade das notas de cinco é:%d' %d)
            elif (a%20)!=0 and (a%20)<5:
                e=(a%20)//1
                print('a quantidade das notas de um é:%d' %e)
elif a<20:
    f=a//10
    print('a quantidade de notas de dez é:%d' %f)
    if a%10!=0:
        g=a//5
        print('a quantidade de notas de cinco é:%d' %g)
        if a%5!=0:
            h=a//1
            print('a quantidade de notas de um é:%d' %h)
    
    
    
    
            
            
        
    
    