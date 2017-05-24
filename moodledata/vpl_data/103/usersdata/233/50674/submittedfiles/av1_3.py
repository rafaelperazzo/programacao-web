# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número: '))
b=int(input('Digite um número: '))
ndedivisoes=0
if b>a:
    maior=b
    menor=a
elif a>b:
    maior=a
    menor=b
while resto>0:
    resto=maior%menor
    maior=menor
    menor=resto
    cont=cont+1
    if resto!=0:
        mdc=resto
print(mdc)
print(cont)    
    



