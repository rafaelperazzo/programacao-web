# -*- coding: utf-8 -*-
a=int(input('Digite um numero binário: '))
soma=0
termo=(a//10)
for i in range(0,10000000000000,1):
    soma=soma+termo*(2**i)
    i=i+1
    termo=termo//10
print(soma)
    


