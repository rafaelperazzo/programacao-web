# -*- coding: utf-8 -*-
import math
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
x=a
y=b
cont=1
while x%y!=0:
    m=x%y
    x=y
    y=m
    
    cont=cont+1
print(y)
print(cont)

  
    