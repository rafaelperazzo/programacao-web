# -*- coding: utf-8 -*-
import math
n = int(input('digite o valor n:'))
soma = 0
denominador = 1
for i in range (1,n+1,1):
    soma = (soma +1)/(denominador)
    denominador = n - denominador
print ('%2f'%soma)



