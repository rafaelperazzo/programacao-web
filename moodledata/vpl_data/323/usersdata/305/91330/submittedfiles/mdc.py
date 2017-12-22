# -*- coding: utf-8 -*-
import math

x = int(input('Digite um número: '))
y = int(input('Digite um número: '))
for n in range (1,x + 1,1):
    if (x%n == 0 and y%n == 0):
        MDC = n
print(MDC)        