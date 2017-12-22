# -*- coding: utf-8 -*-
import math

n = int(input('digite valor de n: '))
a = int(input('digite valor de a: '))
b = int(input('digite valor de b: '))
cont = 0
multiplos = 1

while cont<n:
    if multiplos%a==0 or multiplos%b==0:
        print(multiplos)
        cont+= 1
    multiplos+=1
    
    
