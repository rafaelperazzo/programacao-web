# -*- coding: utf-8 -*-
def verificaPico(lista):
  teste = 0
  for i in range(len(lista)-1):
    if lista[i-1]<lista[i]>lista[i+1]:
      teste = teste+1
  return bool(teste==1)
      
n = int(input(''))
lista = []
for i in range (2):
  lista.append([])
  for j in range(n):
    lista[i].append(int(input('')))
  if verificaPico(lista[i]):
    print('S')
  else:
    print('N')