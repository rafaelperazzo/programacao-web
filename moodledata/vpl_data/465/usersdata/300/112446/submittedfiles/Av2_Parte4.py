# -*- coding: utf-8 -*-
n = int(input('Digite o valor de n: '))
a = []
for i in range(0,n,1):
    linhas = []
    for j in range(0,n,1):
        linhas.append(int(input('Digite um elemento de a: ')))
    a.append(linhas)

c = int(input('Digite o valor de c: '))
b = []
for i in range(0,c,1):
    b.append(int(input('Digite um elemento de b: ')))

s = 0   
for i in range(0,n-1,1):
    s = s + a[i][i+1]
    
print(s)
    