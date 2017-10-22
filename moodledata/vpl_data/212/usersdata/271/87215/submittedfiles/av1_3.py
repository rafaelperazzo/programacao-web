# -*- coding: utf-8 -*-
import math
'''
#ENTRADA
a = int(input('Digite o valor de a : '))
b = int(input('Digite o valor de b : '))
c = int(input('Digite o valor de c : '))
#PROCESSAMENTO
i = 2
while (i>0) :
    if (c>b) and (b>a) :
        if (c%b==0) and (c%a==0) :
            mmc = c
            print(mmc)
            break
    c = c * i
'''

#ENTRADA
a = int(input('Digite o valor de a : '))
b = int(input('Digite o valor de b : '))
c = int(input('Digite o valor de c : '))
#PROCESSAMENTO
i = 2
z = (a*b*c)
while (i<=z) :
    if (i%a==0) and (i%b==0) and (i%c==0) :
        mdc = i
        print(mdc)
        break
    else :
        i = i+1
    

            
        
