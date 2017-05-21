# -*- coding: utf-8 -*-
a=int(input('Digite um numero binário: '))
soma=0
termo=(a//10)
for i in range(0,100000000000000000000000000000000000000000000000000000000000000000000000000000000,1):
    soma=soma+(termo*(2**i))
    soma=soma+1
print(soma)
    
    


