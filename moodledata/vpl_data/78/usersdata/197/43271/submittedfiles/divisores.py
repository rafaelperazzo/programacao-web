# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de múltiplos a serem mostrados:'))
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número'))
i=0
for i in range (1,n+1,1):
    a=a*(i)
    b=b*(i)
    i=i+1
print(a)
print(b)