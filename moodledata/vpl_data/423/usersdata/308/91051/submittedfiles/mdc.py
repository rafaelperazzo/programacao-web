# -*- coding: utf-8 -*-
import math

v = [0, 0]

v[0] = int(input('Informe o primeiro valor: '))
v[1] = int(input('Informe o segundo valor: '))

for i in range(1, min(v)+1, 1):
    if v[0]%i==0 and v[1]%i==0:
        mdc = i
        
print(mdc)
