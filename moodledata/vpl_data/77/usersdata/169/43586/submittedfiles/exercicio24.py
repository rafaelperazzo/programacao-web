# -*- coding: utf-8 -*-
import math
a=int(input('Digite o Primeiro Número Inteiro Positivo:'))
b=int(input('Digite o Segundo Número Inteiro Positivo:'))
mdc=a

while a%mdc!=0 or b%mdc!=0:
    mdc=mdc-1
print(mdc) 
