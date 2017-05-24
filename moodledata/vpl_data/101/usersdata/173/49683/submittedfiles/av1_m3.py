# -*- coding: utf-8 -*-
import math
m=int(input('Digite o número de termos: '))
i=2
soma=0
for i in range(0,m,2):
    pi=4/(i*(i+1)*(i+2))
    soma=pi-(i*(i+1)*(i+2))
print(soma+3)