# -*- coding: utf-8 -*-
import math
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
x=a
y=b
cont=0
while m!=0:
    m=x%y
    x=y
    y=m
    m=x%m
    cont=cont+1
print(m)
print(cont)
  
    