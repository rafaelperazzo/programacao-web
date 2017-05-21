# -*- coding: utf-8 -*-
import math
n=int(input('Digite quantidade de termos: ')) 
soma=0
for i in range (1,n+1,1):
    if i%2==1:
        soma=soma+1/i
    else:
        soma=soma-1/i
print(soma)
