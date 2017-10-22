# -*- coding: utf-8 -*-
import math

#ENTRADA
a = int(input('Digite o valor de a : '))
b = int(input('Digite o valor de b : '))
c = int(input('Digite o valor de c : '))
#PROCESSAMENTO/SAIDA
i = 2
z = (a*b*c)
while (i<=z) :
    if (i%a==0) and (i%b==0) and (i%c==0) :
        mdc = i
        print(mdc)
        break
    else :
        i = i+1
    

            
        
