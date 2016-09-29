# -*- coding: utf-8 -*-
from __future__ import division
import math

a= input('Digite o valor do comprimento a: ')
b= input('Digite o valor do comprimento b: ')
c= input('Digite o valor do comprimento c: ')

if a=b+c or b=c+a or c=a+b:
    print('N')

else:
    print('S')
    if (a)**(2)= (((b)**(2))+((c)**(2))) or (b)**(2)= (((a)**(2))+((c)**(2))) or (c)**(2)= (((b)**(2))+((a)**(2))):
        print ('Re')
    elif (a)**(2)> (((b)**(2))+((c)**(2))) or (b)**(2)> (((a)**(2))+((c)**(2))) or (c)**(2)> (((b)**(2))+((a)**(2))):
        print ('Ob')
    else:
        print ('Ac')
    
    if a=b=c:
        print ('Eq')
    elif (a==b and a!=c) or (a==c and a!=b) or (b==a and b!=c) or (b==c and b!=a) or (c==a and c!=b) or (c==b and c!=a):
        print ('Is')
    else:
        print ('Es')