# -*- coding: utf-8 -*-
n = int(input('Digite um numero qualquer: '))
i = 1
soma = 0

while i<n:
    if n%i==0:
        print('%d'%i)
        soma = soma+i
    
    i = i+1
    
if soma==n:
    print('Perfeito')
    
else:
    print('NÃO PERFEITO')