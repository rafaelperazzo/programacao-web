# -*- coding: utf-8 -*-
n= int(input('Quantidade de elementos de a: '))
m= int(input('Quantidade de elementos de b: '))
a= []
b= []
for i in range(n):
    a.append(int(input('Digite o valor%d de a: ' % i)))
for i in range(m):
    b.append(int(input('Digite o valor%d de b: ' % i)))

while n>0:
    cont= 0
    if a[i] == b[i]:
        cont+=1
        i+=1
    print(cont)



