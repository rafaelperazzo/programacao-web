# -*- coding: utf-8 -*-
import math
n=int(input('Informe o número de termos: '))
a=int(input('Informe o 1° Termo: '))
b=int(input('Informe o 2° Termo: '))

for i in range (1,n+1,1):
    print(a)
    a=a**2
    print(b)
    b=b**2