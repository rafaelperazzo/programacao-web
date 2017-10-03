# -*- coding: utf-8 -*-
import math
n= int(input('Digite a quantidade de múltiplos a ser mostrado: '))
a= int(input('Digite o primero número: '))
b= int(input('Digite o segundo número: '))

mul=2
while ((a%mul==0) and (b%mul==0)):
    print(a)
    print(b)
    mul=mul+1   
