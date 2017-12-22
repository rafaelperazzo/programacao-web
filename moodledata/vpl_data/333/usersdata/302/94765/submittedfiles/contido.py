# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de elementos de n: '))
m = int(input('Digite a quantidade de elementos de m: '))
a = []
b = []
for i in range(0,n,1):
    a.append(int(input('Digite a%d: ' %(i+1))))
for i in range(0,m,1):
    b.append(int(input('Digite b%d: ' %(i+1))))
q = 0
for i in range(0,n,1):
    if a[i] in b:
        q = q+1
print(q)

