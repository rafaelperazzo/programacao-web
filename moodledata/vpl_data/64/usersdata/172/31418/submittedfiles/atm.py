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
        print('%d'c)