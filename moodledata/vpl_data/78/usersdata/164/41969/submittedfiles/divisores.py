# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de múltiplos a serem mostrados: '))
a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
cont=0
i=1
while (cont<n):
    if (i%a==0) or (i%b==0):
        cont=cont+1
        print(i)
    cont=cont+1    