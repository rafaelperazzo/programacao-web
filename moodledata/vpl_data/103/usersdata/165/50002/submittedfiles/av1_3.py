# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0
x=a%b

while resto!=0:
    mdc=b%x
    cont=cont+1
    b=x
    x=mdc
    
print(mdc)
print(cont)

