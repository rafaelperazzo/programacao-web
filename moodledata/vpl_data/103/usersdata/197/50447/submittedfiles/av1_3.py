# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
if b<=a:
    x=b
else:
    x=a
cont=0
mdc=0
divisoes=x
while mdc==0:
    cont=cont+1
    if a%x==0 and b%x==0:
        mdc=x
    else:
        x=x-1
divisoes=divisoes-cont
print(mdc)
print(divisoes)
