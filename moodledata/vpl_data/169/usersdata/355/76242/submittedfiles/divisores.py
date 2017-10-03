# -*- coding: utf-8 -*-
import math
n= int(input('Digite a quantidade de múltiplos a ser mostrado: '))
a= int(input('Digite o primero número: '))
b= int(input('Digite o segundo número: '))

mul=2

for mul in range(mul,n+1,1):    
    if (a%mul==0) or (b%mul==0):
        print(mul)
    else:
        print('Deu errado')
