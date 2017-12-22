# -*- coding: utf-8 -*-

N = int (input('Digite a quantidade de pessoas'))

a = []
soma = 0
i = 0

for i in range (0,N,1):
    T = int (input('Digite o tempo que cada pessoa passou pelo sensor'))
    if (T-10)>i and i!=0:
        soma = soma + T - i - 10
    i = T
    a.append (T)

tempo = a[N-1] + 10 - a[0] - soma
print (tempo)