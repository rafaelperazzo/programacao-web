# -*- coding: utf-8 -*-
#ENTRADA
n = int(input('Digite o valor de um numero : '))
soma = 0
i = 0
#PROCESSAMENTO
while (n/2>0) :
    bin = (n%2) * (10**i)
    soma = soma + bin
    i = i+1
    n = n//10
print(soma)
    



