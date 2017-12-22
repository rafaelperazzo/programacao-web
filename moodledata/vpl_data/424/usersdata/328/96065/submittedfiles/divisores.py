# -*- coding: utf-8 -*-
import math
n=int(input('Número de múltiplos:'))
a=float(input('Número 1:'))
b=float(input('Número 2:'))
cont=0
multiplos=1
while cont<n:
    if multiplos%a==0 or multiplos%b==0:
        print(multiplos)
        cont+= 1
    multiplos+=1