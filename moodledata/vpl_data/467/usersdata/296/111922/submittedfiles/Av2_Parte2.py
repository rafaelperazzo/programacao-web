# -*- coding: utf-8 -*-
n = int(input("Digite a quantidade de elementos da primeira lista: "))
m = int(input("Digite a quantidade de elementos da segunda lista: "))
lista1 = []
lista2 = []
for i in range (0,n,1):
    lista1.append(int(input("Digite um valor para a primeira lista: ")))
for i in range (0,m,1):
    lista2.append(int(input("Digite um valor para a segunda lista: ")))
cont = 0
i = 0
for i in range(0,m,1):
    if lista2[i] in lista1:
        cont += 1
    print(cont)
    i += 1