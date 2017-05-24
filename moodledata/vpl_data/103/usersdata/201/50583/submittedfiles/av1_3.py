# -*- coding: utf-8 -*-
import math
x=int(input('Digite um número:'))
y=int(input('Digite um número:'))
cont=0
if x%y!=0:
    cont=cont=1
    rst=x%y
    x=y
    y=rst
    print(rst)
    print(cont)
    