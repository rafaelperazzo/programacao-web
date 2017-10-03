# -*- coding: utf-8 -*-
import math
n= int(input('Digite a quantidade de múltiplos a ser mostrado: '))
a= int(input('Digite o primero número: '))
b= int(input('Digite o segundo número: '))

for mul in range(2,n,1)    
    if (mul%a==0) and (mul%b==0)):
        print(mul)
        mul=mul+1   
