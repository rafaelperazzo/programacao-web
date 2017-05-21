input# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de termos:'))
termo=1
soma=0
denominador=(termo*termo)
while termo<=n:
    soma=soma+1/denominador
    termo=termo+1
print(soma)    
