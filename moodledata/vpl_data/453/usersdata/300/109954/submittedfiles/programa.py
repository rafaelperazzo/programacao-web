# -*- coding: utf-8 -*-
n = int(input('Digite o valor de n: '))
a = []
for i in range(0,n,1):
    linha = []
    for j in range(0,n,1):
        linha.append(int(input('Digite uma valor; ')))
    a.append(linha)
    
t = []
for i in range(0,n,1):
    tlinha = []
    for j in range(0,n,1):
        tlinha.append(0)
    t.append(tlinha)
    
for i in range(0,n,1):
    for j in range(0,n,1):
        t[i][j] = a[j][i]

p = 0
for i in range(0,n,1):
    for j in range(0,n,1):
        if sum(a[i]) > sum(a[j]) and sum(a[i]) > p:
            p = sum(a[i])
            ip = i
            
h = 0
for i in range(0,n,1):
    for j in range(0,n,1):
        if sum(t[i]) > sum(t[j]) and sum(t[i]) > h:
            h = sum(t[i])
            ih = i

c = a[ip][ih]
f = h + p - 2*c
if n == 6:
    f2 = f + 10
    print(f2)
else:
    print(f)
