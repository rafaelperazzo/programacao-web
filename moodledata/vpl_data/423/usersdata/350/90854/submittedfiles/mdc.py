# -*- coding: utf-8 -*-
import math
n1= int(input('Digite o valor 1(tem que ser maior que 0): '))
n2= int(input('Digite o valor 2(tem que ser maior que 0): '))

x=1
mdc=0

while x<=n1:
    if n1%x==0 and n2%x==0:
        mdc = x
        print(x)
    x = x+1