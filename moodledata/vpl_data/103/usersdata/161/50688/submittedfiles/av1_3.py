# -*- coding: utf-8 -*-
import math
a=int(input('Informe o primeiro número:'))
b=int(input('Informe o segundo número:'))
mdc=b
cont=1
while a%b!=0:
    resto=a%b
    a=b
    b=resto
    cont=cont+1
    mdc=a
print(mdc)
print(cont)
