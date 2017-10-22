# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

a = float(input('Digite o valor de n: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta  = (b**2)-(4*a*c)

if (delta>=0):
    x1 = (-b + ((delta)**(1/2)))/2*a
    x2 = (-b - ((delta)**(1/2)))/2*a
    print (x1)
    print (x2)
    
else:
    print ('SRR')
