# -*- coding: utf-8 -*-
import math
n= int(input('Digite a quantidade de múltiplos a ser mostrado: '))
a= int(input('Digite o primero número: '))
b= int(input('Digite o segundo número: '))
mul=n

for mul in range(n+1,2,-1):    
    if (mul%a==0) and (mul%b==0):
        print(mul)
    else:
        print('Deu errado')
