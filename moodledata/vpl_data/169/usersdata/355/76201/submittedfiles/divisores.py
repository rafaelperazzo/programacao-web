# -*- coding: utf-8 -*-
import math
n= int(input('Digite a quantidade de múltiplos a ser mostrado: '))
a= int(input('Digite o primero número: '))
b= int(input('Digite o segundo número: '))

mul=2
for i in range(2,n,1):
    if a%mul==0 and b%mul==0:
        print(a)
        print(b)
   
