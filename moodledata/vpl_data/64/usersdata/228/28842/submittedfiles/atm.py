# -*- coding: utf-8 -*-
from __future__ import division
import math

valor=int(input('digite o valor a ser sacado:'))
if valor%20>=10: 
    n=int(valor/20)
    print(n)
elif (valor%20)%10>=0:
    x=int(valor%20)/10
    print(x)
elif (valor%20)%10)%5>=0:
    y=int(valor%20)%10)/5
    print(y)
elif(((valor%20)%10)%5)%2>=0:
    z=int(((valor%20)%10)%5)/2
    print(z)
elif((((valor%20)%10)%5)%2)%1>=0:
    w=int((((valor%20)%10)%5)%2)/1
    print(w)