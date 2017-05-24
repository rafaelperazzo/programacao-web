# -*- coding: utf-8 -*-
import math
a=int(input('Informe o primeiro número:'))
b=int(input('Informe o segundo número:'))
mdc=b
cont=0
while mdc%a!=0 or mdc%b!=0:
    mdc=mdc-1
    cont=cont+1
print(mdc)
print(cont)
