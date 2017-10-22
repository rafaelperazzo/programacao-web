# -*- coding: utf-8 -*-
n = int(input("Digite um valor: "))
soma = 0
i = 0
while (n/2>0) :
    bin = (n%2)*(10**1)
    soma = soma + bin
    i = i+1
    n= n//2
print (soma)