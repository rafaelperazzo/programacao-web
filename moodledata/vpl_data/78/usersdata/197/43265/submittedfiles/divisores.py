# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de múltiplos a serem mostrados:'))
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número'))
for i in range (1,n+1,1):
    if a=a*(a+i)>b=b*(b+i):
        i=i+1
        print(a)
    else:
        print(b)