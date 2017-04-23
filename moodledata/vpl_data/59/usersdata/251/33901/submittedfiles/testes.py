# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Digite um numero qualquer: '))
decisao = 0
i = 2
soma = 1
while i<n:
    if n%i==0:
        print('%d'%i)
        soma = soma+i
    i=i+1
    
if soma==n:
    print('Perfeito')
    
else:
    print('Não perfeito')
    
    
