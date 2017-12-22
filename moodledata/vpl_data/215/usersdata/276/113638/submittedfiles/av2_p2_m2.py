# -*- coding: utf-8 -*-

portas = int(input('Digite a quantidade de portas:'))

vidas = []

for i in range (0,portas, 1):
    vida = int (input ('Digite a quantidade de vidas: '))
    vidas.append (vida)
    
entrada = int (input('Digite o indice da entrada: '))
saida = int (input('Digite o indice da saida:'))

soma = 0

for i in range  (entrada, saida + 1,1):
    soma = soma + a[i]
    
print (soma)