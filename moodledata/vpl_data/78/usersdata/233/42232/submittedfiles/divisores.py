# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de divisrorer que será mostrada: '))
a=int(input('Digite um número qualquer: '))
b=int(input('Digite um número qualquer: '))
cont=0
i=0
while cont<n:
    if i%a==0 or i%b==0:
        print(1)
        cont=cont+1
    i=i+1    