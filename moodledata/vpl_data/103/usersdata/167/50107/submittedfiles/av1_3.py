# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
um=a
dois=b
s=um%dois
contador=1
while s!=0:
    um=dois
    dois=s
    s=um%dois
    contador=contador+1
print(dois)
print(contador)