# -*- coding: utf-8 -*-
import math
x=int(input('Digite um número:'))
y=int(input('Digite um número:'))
pst=x
atc=y
rst=pst%act
while rst!=0:
    pst=rst
    act=rst
    rst=pst%act
print(act)