# -*- coding: utf-8 -*-

n = int (input('Quantidade de portas:'))

a = []

for i in range (0,n,1):
    vidas = int(input('Vidas:'))
    a.append (vidas)
    
entrada = int (input('entrada'))
saida = int (input('saida'))

soma = 0

for i in range (entrada,saida + 1, 1):
    soma = soma + a[i]
    
print (soma)