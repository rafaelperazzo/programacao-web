# -*- coding: utf-8 -*-
numero=int(input('Informe um número decimal: '))
i=0
soma=0
while n>0:
    m=numero%2
    soma=soma+m*(10**i)
    n=n%10
    i=i+1
print(soma)

