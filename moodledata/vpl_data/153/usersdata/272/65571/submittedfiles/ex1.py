# -*- coding: utf-8 -*-
a= float(input('Digite o valor de a:'))
b= float(input('Digite o valor de b:'))
c= float(input('Digite o valor de c:'))

DELTA= (b**2)-(4*a*c)

if DELTA>=0:
    x1= (-b+((DELTA)**(1/2)))/(2*a)
    x2= (-b-((DELTA)**(1/2)))/(2*a)
    print('%.2f' %x1)
    print('%.2f' %x2)
    
if DELTA<0:
    print('SRR')
