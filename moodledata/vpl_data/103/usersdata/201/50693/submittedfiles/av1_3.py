# -*- coding: utf-8 -*-
import math
x=int(input('Digite um número:'))
y=int(input('Digite um número:'))
cont=1
while x%y!=0:
    res=x%y
    x=y
    y=res
    cont=0+1
    print(res)