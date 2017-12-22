# -*- coding: utf-8 -*-
n = int(input('insira a quantidade de elementos:'))
lista = []
for i in range (n):
  lista.append(int(input('digite os elementos')))
listaimpar =[]
listapar = []
for i in range (n):
  if lista[i]%2 == 0:
    listapar.append(lista[i])
  else:
    listaimpar.append(lista[i])
print(sum(listaimpar))
print(sum(listapar))
print(len(listaimpar))
print(len(listapar))

