# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de múltiplos a serem mostrados:'))
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número'))

contador=0
i=1

while contador<n:
    if i%a==0 or i%b==0:
        print(i)
        contador=contador+1
    i=i+1
    