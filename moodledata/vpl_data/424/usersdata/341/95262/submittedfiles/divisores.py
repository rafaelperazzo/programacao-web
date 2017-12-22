# -*- coding: utf-8 -*-
import math

n = int(input('Digite o valor de n: '))
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
x=1
cont=0
while (cont<n):
    if(x%a)==0 or (x%b)==0:
        print(x)
        x = x+1
        cont = cont+1
    else:
        x = x + 1

