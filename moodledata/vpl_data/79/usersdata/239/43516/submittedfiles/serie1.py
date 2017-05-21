# -*- coding: utf-8 -*-
import math
n=int(input("digite o numero de termoz da cequencia:"))
zoma=0
numerador=1
for i in range(1,1+n,1):
    if i%2==0:
        zoma=zoma-(numerador/(numerador**2))
    else:
        zoma=zoma+(numerador/(numerador**2))
    numerador=numerador+1
print("%.5f"%zoma)
