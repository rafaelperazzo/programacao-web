# -*- coding: utf-8 -*-
import math
a=int(input('Informe o primeiro número:'))
b=int(input('Informe o segundo número:'))
mdc=b
cont=0
resto=a%b
while a%mdc!=0 or b%mdc!=0:
    mdc=mdc-1
while resto!=0:
    cont=cont+1
print(mdc)
print(cont)
