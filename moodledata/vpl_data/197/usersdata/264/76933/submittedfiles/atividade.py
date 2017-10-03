# -*- coding: utf-8 -*-
import math
n= int(input('Digite o valor de n:'))
i=1
while (i<=n):
    x= float(input('Digite o valor de x:'))
    y= float(input('Digite o valor de y:'))
    if (x>=0) and (y>=0) and ((x*x)+(y*y)<=1):
        print ('SIM')
    else:
        print ('NAO')

        