# -*- coding: utf-8 -*-
import math

a = int(input('insira o primeiro número:'))
b = int(input('insira o segundo número:'))
 
while b!=0:
    resto = a%b
    a = b
    b = resto
    
print (a)


