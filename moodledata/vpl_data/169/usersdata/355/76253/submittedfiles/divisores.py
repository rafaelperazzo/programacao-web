# -*- coding: utf-8 -*-
import math
n= int(input('Digite a quantidade de múltiplos a ser mostrado: '))
a= int(input('Digite o primero número: '))
b= int(input('Digite o segundo número: '))

mul=2
cont=1
for mul in range(mul,(n+cont),1):    
    if (mul%a==0) or (mul%b==0):
        print(mul)
        cont=cont+1
    else:
        print('Deu errado')
