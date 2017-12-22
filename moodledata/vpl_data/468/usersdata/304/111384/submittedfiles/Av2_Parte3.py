# -*- coding: utf-8 -*-
m = int(input('Quantas listas: '))
n = int(input('Qntd elemento listas: '))
for i in range (0,m,1):
    lista=[]
    for j in range (0,n,1):
        lista.append(int(input('Elemento: ')))

media = len(lista)/n
print(lista)
