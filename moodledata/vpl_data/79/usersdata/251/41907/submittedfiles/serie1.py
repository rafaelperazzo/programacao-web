# -*- coding: utf-8 -*-
import math
n = int(input('Digite um numero de termos: '))
num = 1
den=num**2
soma=0
termo=num/den
for i in range(1,n+1,1):
    if num%2==0:
        soma=soma-termo
    else:
        soma=soma+termo
    num=num+1
    den=num**2
    termo=num/den
print('%.5f'%soma)        
    

