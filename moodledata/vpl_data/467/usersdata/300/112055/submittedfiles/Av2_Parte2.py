# -*- coding: utf-8 -*-
n = int(input('Digite o valor de n: '))
m = int(input('Digite o valor de m: '))
a = []
b = []
for i in range(0,n,1):
    a.append(int(input('Digite um elemento de a: ')))
for i in range(0,n,1):
    b.append(int(input('Digite um elemento de b: ')))
    
cont = 0    
for i in range(0,n,1):
    if b[i] in a:
        cont = cont + 1

print(cont)

