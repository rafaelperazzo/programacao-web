# -*- coding: utf-8 -*-
n=int(input('Digite o numero binario: '))
soma=0
expoente=0
while(n>0):
    resto=n%2
    soma=soma+(resto*2**expoente)
    n=n//2
print(soma)
    
    


