# -*- coding: utf-8 -*-
import math
x=int(input('Digite um número:'))
y=int(input('Digite um número:'))
rst=x%y
while rst!=0:
    x=y
    y=rst
    rst=x%y
print(rst)