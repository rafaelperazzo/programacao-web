# -*- coding: utf-8 -*-
import math
a=int(input('Informe o primeiro número:'))
b=int(input('Informe o segundo número:'))
mdc=b
cont=1
while a%mdc!=0 or b%mdc!=0:
    mdc=mdc-1
while a%b!=0:
    resto=a%b
    b=resto
    a=b
    cont=cont+1
print(mdc)
print(cont)
