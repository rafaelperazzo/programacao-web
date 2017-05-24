# -*- coding: utf-8 -*-
import math
a=int(input('digite o primeiro valor:'))
b=int(input('digite o segundo valor:'))
if a>b:
    maior=a
    menor=b
else:
    maior=b
    menor=a
contador=0
while maior%menor!=0:
    x=maior%menor
    maior=menor
    menor=x
    contador=contador+1
    mdc=x
    print(contador)
    print(mdc)
    
    
