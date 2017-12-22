# -*- coding: utf-8 -*-
n = int(input('pessoas : '))
z = 0
soma = 0
a = []
for i in range (0,n,1) :
    t = int(input('Digite o instante : '))
    if (t-10)>z and (z!=0) :
        soma = soma + t - z - 10
    z = t
    a.append(t)
resposta = a[n-1] + 10 - a[0] - soma
print(resposta)
