# -*- coding: utf-8 -*-
a=int(input('Digite um numero binário: '))
soma=0
termo=(a//10)
for i in range(0,i,1):
    soma=soma+(termo*(2**i))
    soma=soma+1
    termo=termo//10
print(soma)
    
    


