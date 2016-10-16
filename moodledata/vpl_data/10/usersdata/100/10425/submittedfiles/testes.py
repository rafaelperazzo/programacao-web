# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
x =0
n = input('digite o valor de n:')
cont = 0
while x <n:
    num=input ('digite o valor:')
    if num == cont:
        cont = cont +1
        print cont
    if num !=cont:
        cont = cont +num
    x = x+1
    