# -*- coding: utf-8 -*-
c = int(input('Digite o número de consultas: '))
lista =[]
for i in range(c):
    lista.append(int(input()))
lista2 =[]
lista2 = (list(set(lista)))
a = len(lista2)*2
print(a)
    

        