# -*- coding: utf-8 -*-
soma=0
n=10000000
x=int(input(''))
for i in range(0,8,1):
    i=i+1
    soma=(x//n)+soma
    x=x%n
    n=n/10
print(soma)    
    
    