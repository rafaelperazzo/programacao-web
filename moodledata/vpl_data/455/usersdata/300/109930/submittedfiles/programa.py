# -*- coding: utf-8 -*-
while True:
    n = int(input('Digite o valor de n: '))
    if n >= 3:
        break

a = []
for i in range(0,n,1):
    linha = []
    for j in range(0,n,1):
        linha append(int(input('Digite um elemento da matriz: ')))
    a.append(linha)
    
l = 0
for i in range(0,n,1):
    if sum(a[i]) != sum(a[j]):
        l = i
        break
    break

b = []
c = 0
for i in range(0,n,1):
    soma = 0
    for j in range(0,n,1):
        soma = soma + a[j][i]
    if soma == sum(b):
        b= []
    elif soma != sum(b):
        if sum(b) != 0:
            continue
        for k in range(0,n,1):
            b.append(matriz[k][i])
            c = i

lt = []
for i in range(0,n,1):
    lt.append(sum(a[i]))
lt = sorted(lt)
print(a[l][c] + (lt[1] - sum(a[l])))
print(a[l][c])

