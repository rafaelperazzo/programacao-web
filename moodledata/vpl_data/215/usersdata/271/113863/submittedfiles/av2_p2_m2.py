# -*- coding: utf-8 -*-
#ENTRADA
n = int(input('Digite a quantidade de portas : '))
a = []
#PROCESSAMENTO
for i in range (0,n,1) :
    v = int(input('Vidas : '))
    a.append(v)
x = int(input('Porta de Entrada : '))
y = int(input('Porta de Saída : '))
soma = 0
for i in range (x,y+1,1) :
    soma = soma + a[i]
print(soma)

