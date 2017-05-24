# -*- coding: utf-8 -*-
import math
a=int(input('digite um numero:'))
b=int(input('digite um numero:'))
resto=a%b
cont=0
mdc=a/b
while resto>0:
    mdc=a/b
    cont=cont+1
    a=b
    b=resto
if resto==0:
    print(mdc)
    print(cont)
