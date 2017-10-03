# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
v = int(input('valor a ser sacado: '))
if v>=20 :
    x=v//20
    print(x)
    if v%20>=10 :
        y=(v%20)//10
        print(y)
    else :
        print(0)
        if v%20>=5 :
            u=(v%20)//5
            print(u)
        else :
            print(0)