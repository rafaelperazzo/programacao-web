# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de multiplos a serem mostrados:'))
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número:'))
contador=0
multiplo=1
while contador<n:
    if multiplo%a==0 or multiplo%b==0:
        print(multiplo)
        contador=contador+1
    multiplo=multiplo+1
    