# -*- coding: utf-8 -*-

N = int (input('Digite a quantidade de pessoas'))

a = []
b = []
soma = 0
x = 0

for i in range (0,N,1):
    T = int (input('Digite o tempo que cada pessoa passou pelo sensor'))
    a.append (T+10)
    
for i in range (0,N,1):
    if a[i+1] > a[i]:
        soma = soma + a[i+1] + (a[i+1] - a[i])
    elif a[i+1] < a[i]:
        soma = soma + a[i] + (a[i] - a[i+1])    
    b.append (soma)
    
tempo = max (b)
respota = tempo - a[0] - 10
print (resposta)