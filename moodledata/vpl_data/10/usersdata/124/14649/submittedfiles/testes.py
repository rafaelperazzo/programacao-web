# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
a = input('')
b = input('')
c = input('')

if a > b:
    if (c%a)%b == 0:
        print(c//a)
        print((c%a)//b)
    else:
        print('N')
elif b > a:
    if (c%b)%a == 0:
        print(c//b)
        print((c%b)//a)
    else:
        print('N')