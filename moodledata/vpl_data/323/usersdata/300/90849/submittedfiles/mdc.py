# -*- coding: utf-8 -*-
import math

x = int(input('Digite um número inteiro positivo: '))
y = int(input('Digite um número inteiro positivo: '))
n = 2
while x%n == 0 and y%n == 0:
    x = x/n
    y = y/n
    if x%n != 0 and y%n != 0:
        n = n+1
    while x == y:
        print(n)
        break
        
