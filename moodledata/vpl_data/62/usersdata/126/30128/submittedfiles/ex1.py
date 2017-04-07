# -*- coding: utf-8 -*-

a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!

Delta= (b**2)-(4*a*c)

x1= (-b+((Delta)**(1/2)))/(2*a)
x2= (-b-((Delta)**(1/2)))/(2*a)

if Delta>=0:
    print(x1)
    print(x2)
else:
    print('SRR')
    
