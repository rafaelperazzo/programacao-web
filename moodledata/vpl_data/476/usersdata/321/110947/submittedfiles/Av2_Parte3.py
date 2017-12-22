# -*- coding: utf-8 -*-
n= int(input('Quantidade de elementos de a: '))
m= int(input('Quantidade de elementos de b: '))
a= []
b= []

for i in range(n):
    a.append(int(input('Digite o valor%d de a: ' % i)))
for j in range(m):
    b.append(int(input('Digite o valor%d de b: ' % j)))
    soma = 0
    while a[i] == b[j]:
        soma+=1
        i+=1
    print(soma)



