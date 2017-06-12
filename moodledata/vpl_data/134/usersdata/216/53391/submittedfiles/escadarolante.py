# -*- coding: utf-8 -*-
soma=10

n=int(input('Digite o número de pessoas:'))
t=int(input('Digite o instante:'))
a=t
for i in range(1,n+1,1):
    b=int(input('Digite o instante:'))
    soma= soma + (b-a)
    a=b
   
    
    
    
print(soma)