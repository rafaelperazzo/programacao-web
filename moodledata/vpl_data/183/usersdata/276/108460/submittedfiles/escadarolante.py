# -*- coding: utf-8 -*-

N = int (input('Digite a quantidade de pessoas'))

a = []
soma = 0
x = 0

for i in range (0,N,1):
    T = int (input('Digite o tempo que cada pessoa passou pelo sensor'))
    if (T-10) >= x and x !=0:
        soma = soma + T - x - 10
    x = T
    a.append (T)

tempo = a[N-1] + 10 - a[0] - soma
print (tempo)