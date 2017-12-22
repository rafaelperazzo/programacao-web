# -*- coding: utf-8 -*-
import math
x = int(input('Digite o valor de n: '))
y = int(input('Digite o valor de a: '))
z = int(input('Digite o valor de b: '))
cont = 0
multiplos = 1
while cont<x:
    if multiplos%y==0 or multiplos%z==0:
        print(multiplos)
        cont += 1
    multiplos += 1

