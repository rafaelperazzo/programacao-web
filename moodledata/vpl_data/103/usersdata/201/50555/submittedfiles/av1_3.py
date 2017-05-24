# -*- coding: utf-8 -*-
import math
x=int(input('Digite um número:'))
y=int(input('Digite um número:'))
cont=1
if x%y!=0:
    rst=x%y
    x=y
    y=rst
    cont=0+1
    print(rst)
    print(cont)