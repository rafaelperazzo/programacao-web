# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

i=float(input('digite o valor inicial do investimento: '))
t=float(input('digite a taxa de crescimento percentual: '))

while t<0 or t>1:
    t=float(input('digite a taxa de crescimento percentual: '))

while i:
    print(i)
    i=i+(t*i)
    if (t = 10**(-10):
        break