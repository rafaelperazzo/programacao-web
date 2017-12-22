moment# -*- coding: utf-8 -*-
c = int(input())
lista =[]
for i in range(c):
    lista.append(int(input()))
lista2 =[]
for i in range(c):
    if lista[i] not in lista:
        lista2.apeend(lista[i])
a = (len(lista2)*2)
print(a)