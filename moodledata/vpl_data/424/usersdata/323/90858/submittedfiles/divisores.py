# -*- coding: utf-8 -*-
import math
n= int(input('Digite o valor n: '))
a= int(input('Digite o valor a: '))
b= int(input('Digite o valor b: '))

x=1
cont=1

while cont<=n:
    if x%a==0 or x%b==0:
        print(x)
        x=x+1
        cont=cont+1
    else:
        x=x+1