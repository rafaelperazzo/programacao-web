# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
cont = 0
x = 10
b = input ('num:')
while True:
    b%10!=0
    b = b%10
    cont = cont +1
    if b%10==0:
        break
    print cont
    