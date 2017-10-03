# -*- coding: utf-8 -*-
a = float(input('Digite o valor do coeficiente a da equação: '))
b = float (input('Digite o valor do coeficiente b da equação: '))
c =  flaot (input('Digite o valor do coeficiente c da equação: '))

delta = (b*b) - 4*a*c

if (delta<0):
    print ('SRR')
else:
    x1 = (-b + (delta**(1/2)))/2*a
    x2 = (-b - (delta**(1/2)))/2*a
    print (x1)
    print (x2)
    
