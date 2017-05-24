# -*- coding: utf-8 -*-
import math
a=int(input('Digite a:'))
b=int(input('Digite b:'))
cont=1
while (a%b)>0:
    resto=a%b
    mdc=resto
    cont=cont+1
    a=b
    b=resto
print(mdc) 
print(cont)
    