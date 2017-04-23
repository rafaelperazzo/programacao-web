# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
saque=int(input('digite o valor do saque:'))
if  saque/20:
    a=(saque/20)
    b=(saque%20)
    print('%d'%a)
    if  b/10:
        c=(b/10)
        d=(b%10)
        print('%d'%c)
        if  d/5:
            e=(d/5)
            f=(d%5)
            print('%d'%e)
            if  f/2:
                g=(f/2)
                h=(f%2)
                print('%d'%g)
        