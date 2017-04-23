# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor=int(input('Digite o valor do saque: '))
n=((valor/20)-(valor%20))
x=((valor%20)/10)
if valor%20==0:
    print(n)
    print(x)
if valor%20!=0:
    print(n)
    print(x)