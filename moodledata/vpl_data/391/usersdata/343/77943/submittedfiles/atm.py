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
        if v%20>=5 :
            u=(v%20)//5
            print(u)
            if v%20>=2 :
                w=(v%20)//2
                print(w)
                if v%20>=1 :
                    z=(v%20)//(v%20)
                    print(z)