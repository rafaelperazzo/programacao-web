# -*- coding: utf-8 -*-
a=int(imput('Digite um numero binário: '))
soma=0
termo=a//10
for i in range(0,1+1,1):
    soma=soma+(termo*(2**i))
    soma=soma+1
print(soma)
    
    


