# -*- coding: utf-8 -*-
n=int(input('digite um número binário:'))
i=0
soma=0
while n>0:
    b=n%10
    n=n//10
    soma=b*(10**i)
    i=i+1
print(soma)    
    
    
    
    
    