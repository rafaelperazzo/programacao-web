# -*- coding: utf-8 -*-
qa= int(input('Quantidade de elementos de a: '))
qb= int(input('Quantidade de elementos de b: '))
a= []
b= []
for i in range(qa):
    a.append(int(input('Digite o valor%d de a: ' % i)))
    for j in range(qb):
        b.append(int(input('Digite o valor%d de b: ' % j)))
