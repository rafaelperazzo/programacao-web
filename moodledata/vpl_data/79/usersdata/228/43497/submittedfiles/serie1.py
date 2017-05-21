input# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de termos:'))
termo=1
soma=0
denominador=(termo*termo)
while termo<=n:
    termo=termo+1
    soma=termo/denominador
    denominador=(termo*termo)
    if termo%2==0:
        termo=termo*1
    else:
        soma=termo*(-1)
print(soma)    
