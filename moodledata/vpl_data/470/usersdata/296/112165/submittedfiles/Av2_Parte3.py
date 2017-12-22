# -*- coding: utf-8 -*-
n = int(input("Digite a quantidade de elementos da lista: "))
m = int(input("Digite a quantidade de listas que você deseja: "))
cont = 0
while cont<=m:
    lista = []
    for i in range (0,n,1):
        lista.append(int(input("Digite um elemento para a lista: ")))
        cont += 1
print(lista)        