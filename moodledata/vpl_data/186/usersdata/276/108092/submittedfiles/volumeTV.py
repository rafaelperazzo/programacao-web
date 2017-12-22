 -*- coding: utf-8 -*-
V = int(input ('Digite o volume inicial: '))
T = int(input ('Digite a quantidade de mudanças: '))

a = []

for i in range (0, T, 1):
    volume = int (input('Digite o volume: '))
    a.append (volume)
    
som = 0

for i in range (0, T, 1):
    soma = soma + a[i]
    
print (soma)