# -*- coding: utf-8 -*-
soma=10
a=0
n=int(input('Digite o número de pessoas:'))
t1=int(input('Digite o instante:'))
soma=soma+a
b=t1
for i in range(1,n,1):
    t=int(input('Digite o instante:'))
    soma=soma+(t-b)
    b=t
   
    
print(soma)