# -*- coding: utf-8 -*-
from __future__ import division
import math

valor=int(input('digite o valor a ser sacado:'))
    n=int valor/20
    print(n)
    x=int(valor%20)/10
    print(x)
    y=int((valor%20)%10)/5
    print(y)
    z=int(((valor%20)%10)%5)/2
    print(z)
    w=int((((valor%20)%10)%5)%2)/1
    print(w)