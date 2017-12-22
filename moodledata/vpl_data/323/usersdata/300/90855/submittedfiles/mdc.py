# -*- coding: utf-8 -*-
import math

x = int(input('Digite um número inteiro positivo: '))
y = int(input('Digite um número inteiro positivo: '))
n = 2
m = 1
for i in range(0,x == y,0):
    while x%n == 0 or y%n == 0:
        x = x/n
        y = y/n
        if x%n != 0 or y%n != 0:
            m = n*m
            n = n+1
print(m)
   
