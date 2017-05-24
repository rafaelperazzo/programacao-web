# -*- coding: utf-8 -*-
import math
m=int(input('Digite o número de termos: '))
i=2
for i in range(0,m,2):
    pi=4/(i*(i+1)*(i+2))+soma
    i=i+2
    soma=pi-(4/(i*(i+1)*(i+2)))
r=soma+3
print('%.6f'%r)