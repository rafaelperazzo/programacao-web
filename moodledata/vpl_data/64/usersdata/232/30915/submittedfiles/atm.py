# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor=int(input('Digite o valor do saque: '))
if valor%20==0:
    n=(valor/20):
        print(n)
    x=((valor%20)/10):
        print(x)
    y=(((valor%20)%10)/5):
        print(y)
    z=((((valor%20)%10)%5)/2):
        print(z)
    u=(((((valor%20)%10)%5)%2)/1):
        print(u)