# -*- coding: utf-8 -*-

n = int(input('Digite o numero binario:'))
i = 0
soma = 0

while (n>0):
    ultimo = n%10
    normal = ultimo * (2**i)
    soma = soma + normal
    i = i+1
    
print (soma)
    