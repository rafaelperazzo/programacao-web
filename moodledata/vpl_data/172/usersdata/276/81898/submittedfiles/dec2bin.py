# -*- coding: utf-8 -*-
n = int (input('Digite o numero binario: '))
i = 0
soma = 0

while (n/2>0):
    resto  = (n%2)
    binario = resto*(10**i)
    soma = soma + binario
    n = n//2
    i = i +1

print (soma)
    