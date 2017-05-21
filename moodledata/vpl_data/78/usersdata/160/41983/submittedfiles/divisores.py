# -*- coding: utf-8 -*-
import math

n=int(input('Digite o número de múltiplos:'))
a=int(input('Digite a:'))
b=int(input('Digite b:'))
cont=0
i=1
while cont<n:
    if i%a==0 or i%b==0:
        cont=cont+1
        print(i)
    i=i+1
