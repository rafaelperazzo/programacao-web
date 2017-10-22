# -*- coding: utf-8 -*-
import math
n=int(input("Digite n: "))
a=int(input("Digite a: "))
b=int(input("Digite b: "))
if a>=b:
    pa=b
if a<b:
    pa=a
cont=0
for i in range (pa,10000,1):
    if i%a==0 or i%b==0:
        print i
        cont=cont + 1
        if cont==n:
            break