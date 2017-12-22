# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de elementos de a: ''))
m = int(input('Digite a quantidade de elementos de b: ''))
a = []
b = []
cont = 0
for i in range (0,n,1):
    a.append(int(input('Digite os elementos de a: ')))
for i in range (0,n,1):
    b.append(int(input('Digite os elementos de b: ')))    
for i in range (0,n,1):
    if a[i] in b:
        cont = cont + 1
print(cont)        
