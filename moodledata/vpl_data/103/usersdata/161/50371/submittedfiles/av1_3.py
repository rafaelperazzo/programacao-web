# -*- coding: utf-8 -*-
import math
a=int(input('Informe o primeiro número:'))
b=int(input('Informe o segundo número:'))
mdc=b
cont=0
while a%mdc!=0 or b%mdc!=0:
    mdc=mdc-1
for i in range(a,b+1,1):
    resto=a%b
    b=resto
    a=b
    print(b)
    print(a)
    cont=cont+1
print(mdc)
print(cont)
