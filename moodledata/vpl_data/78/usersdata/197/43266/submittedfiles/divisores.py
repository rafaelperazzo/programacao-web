# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de múltiplos a serem mostrados:'))
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número'))
for i in range (1,n+1,1):
    a=a*(a+i)
    b=b*(b+i)
    if a>b:
        print(a)
    else:
        print(b)