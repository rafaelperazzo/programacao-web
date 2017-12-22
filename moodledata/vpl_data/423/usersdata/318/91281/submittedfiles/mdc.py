# -*- coding: utf-8 -*-
import math

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

def mdc(a, b):
    resto = 0
    while(b > 0) :
        resto = b
        b = a % b
        a = resto
    return a
    
print('MDC: ',mdc(num1, num2))