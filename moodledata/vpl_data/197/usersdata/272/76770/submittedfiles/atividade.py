# -*- coding: utf-8 -*-
import math

n= int(input('Digite o valor de n: '))
x= float(input('Digite x: '))
y= float(input('Digite y: '))
i=1
if (n==1):
    if (x>=0) and (y>=0) and (((x**2) + (y**2))<=1):
        print('SIM')
    else:
        print('NAO')
    
else:
   while (i<=n):
        if (x>=0) and (y>=0) and (((x**2) + (y**2))<=1):
            print('SIM')
        
        else:
            print('NAO')
        i=i+1
   
    
