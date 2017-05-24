# -*- coding: utf-8 -*-
import math

m=int(input('digite o valor de m:'))
c=4
cont=o
a=0
b=2

for i in range (0,m,1):
    a=4/(b*(b+1)*(b+2))
    cont=cont+1
    if (cont%2==0):
        c=c-a
    if ( cont%2==1):
        c=c+a
    b=b+2
            
 print ('%.6'%a)
        