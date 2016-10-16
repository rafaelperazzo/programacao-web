# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
x =1
c = 1
b = input('digite um num:')
while True:
    if b%10!=0:
        b=b//10
        c = c+b
        break
    print c