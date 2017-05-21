# -*- coding: utf-8 -*-
n=int(input('digite o seu numero na base binaria:'))
soma=0
i=0
while (n/10)>0:
    A=n%10
    soma=soma+(A*(2**i))
    n=n//10
    i=i+1
print(soma)    
    
    
    