# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de múltiplos a serem mostrados: '))
a=int(input('Digite número 1: '))
b=int(input('Digite o número 2: '))
i=1
cont=0
while (cont<n):
    if (i%a==0) or (i%b==0):
        cont=cont+1
        print(i)
    i=i+1    

