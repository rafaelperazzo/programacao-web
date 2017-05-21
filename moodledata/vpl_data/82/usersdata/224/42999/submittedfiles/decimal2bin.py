# -*- coding: utf-8 -*-
n=int(input('Digite um numero binário: '))
soma=0
i=0
m=n%10
while n>0:
    soma=soma+m*2**1
    n=n//10
    i=i+1
print(soma)

    


