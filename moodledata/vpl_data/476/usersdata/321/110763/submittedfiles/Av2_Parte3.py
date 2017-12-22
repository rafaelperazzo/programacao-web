# -*- coding: utf-8 -*-
qa= int(input('Quantidade de elementos de a: '))
qb= int(input('Quantidade de elementos de b: '))
a= []
b= []

for i in range(qa):
    a.append(int(input('Digite o valor%d de a: ' % i)))
    
for i in range(qb):
    b.append(int(input('Digite o valor%d de b: ' % i)))
    soma= 0
    if a[i] == b[i]:
        soma+=1
        i+=1
    print(i)

