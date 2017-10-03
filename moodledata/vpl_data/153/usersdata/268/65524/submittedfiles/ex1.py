# -*- coding: utf-8 -*-
a= float(input(' Digite a :'))
b= float(input(' Digite b :'))
c= float(input(' Digite c :'))

Delta= b*b -4*a*c

if (Delta<0):
    print('SRR')
if (Delta >= 0):
    
    X1= (b + (Delta)**(1/2))/(2*a)
    X2= (b - (Delta)**(1/2))/(2*a)
    print(X1)
    print(X2)