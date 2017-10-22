# -*- coding: utf-8 -*-
n=int(input('Digite o numero binario: '))
soma=0
expoente=0
while(n>0):
    resto=n%10
    soma=soma+(resto*(2**expoente))
    n=n//10
    expoente=expoente+1
print(soma)
    
    


