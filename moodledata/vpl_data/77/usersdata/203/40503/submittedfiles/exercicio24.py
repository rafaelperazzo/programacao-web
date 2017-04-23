# -*- coding: utf-8 -*-
import math
n1=int(input('digite o primeiro valor: '))
n2=int(input('digite o segundo valor: '))
if n1<=n2:
    for i in range(1,n1,1):
        if n1%i==0 and n2%i==0:
            mdc=i
    print(mdc)
else:
    for i in range(1,n2,1):
        if n1%i==0 and n2%i==0:
            mdc=i
    print(mdc)