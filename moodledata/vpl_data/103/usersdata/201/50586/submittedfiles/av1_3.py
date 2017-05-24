# -*- coding: utf-8 -*-
import math
x=int(input('Digite um número:'))
y=int(input('Digite um número:'))
cont=0
if x%y!=0:
    rst=x%y
    x=y
    y=rst
    cont=cont=1
    print(rst)
    print(cont)
    