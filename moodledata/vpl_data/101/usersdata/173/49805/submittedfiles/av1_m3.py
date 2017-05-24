# -*- coding: utf-8 -*-
import math
m=int(input('Digite o número de termos: '))
i=2
soma=0
for i in range(2,m,1):
    pi=4/(i*(i+1)*(i+2))+soma
    i=i+2
    soma=pi-(4/(i*(i+1)*(i+2)))
r=soma+3
print('%.6f'%r)