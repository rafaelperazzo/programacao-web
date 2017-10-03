# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#ENTRADA
a= input('Digite A: ')
b= input('Digite B: ')
c= input('Digite C: ')

x= (b**2)-(4*a*c) 
x=math.sqrt(x) 

if x<0 :
    print('SRR')
else :
    x=(b**2)-(4*a*c)
    x1=(-b+x**1/2)/2*a
    x2=(-b-x**1/2)/2*a
    print(x1 and x2)