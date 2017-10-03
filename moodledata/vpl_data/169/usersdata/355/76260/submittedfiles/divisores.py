# -*- coding: utf-8 -*-
import math
n= int(input('Digite a quantidade de múltiplos a ser mostrado: '))
a= int(input('Digite o primero número: '))
b= int(input('Digite o segundo número: '))
n=n+4
mul=2
cont=0
for mul in range(mul,(n+cont),1):    
    if (mul%a==0) or (mul%b==0):
        print(mul)
        if mul%a==0 and mul%b==0:
            cont=cont+2
        else:
            cont=cont+1
