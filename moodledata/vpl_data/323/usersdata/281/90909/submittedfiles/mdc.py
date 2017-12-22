# -*- coding: utf-8 -*-
import math
x = int (input('Digite um número: '))
y = int (input('Digite outro número: '))

mdc=x
while x % mdc!=0 or y % mdc!=0:
    mdc=mdc-1
    print(mdc)
    

    




