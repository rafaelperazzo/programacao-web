# -*- coding: utf-8 -*-
import math
n= int(input('Digite a quantidade de múltiplos a ser mostrado: '))
a= int(input('Digite o primero número: '))
b= int(input('Digite o segundo número: '))

mul=2
while ((mul%a==0) and (mul%b==0)):
    print(a)
    print(b)
    mul=mul+1   
