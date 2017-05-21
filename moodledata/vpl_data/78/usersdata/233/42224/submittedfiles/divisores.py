# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de divisrorer que será mostrada: '))
a=int(input('Digite um número qualquer: '))
b=int(input('Digite um número qualquer: '))
cont=1
while cont%a==0 or cont%b==0:
        print(cont)
    cont=cont+1