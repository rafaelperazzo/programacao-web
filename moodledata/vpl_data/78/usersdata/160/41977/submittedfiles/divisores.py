# -*- coding: utf-8 -*-
import math

n=int(input('Digite o número de múltiplos:'))
a=int(input('Digite a:'))
b=int(input('Digite b:'))
cont=0
i=1
while cont<n:
    if a%i==0 and b%i==0:
        cont=cont+1
        print(i)
    print(i)
