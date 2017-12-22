# -*- coding: utf-8 -*-
n = int(input('insrira a ordem da matriz: '))

matriz = []
for i in range (0,n,1):
    l = []
    for j in range (0,n,1):
        val = int(input('digite os elementos da amtriz:'))
        l.append(val)
    matriz.append(l)
    
lista = []

for i in range (0,n,1):
  soma = 0
  for j in range (0,n,1):
    soma = (soma + matriz[i][j])
  lista.append(soma)
  
for j in range (0,n,1):
  soma = 0
  for i in range (0,n,1):
    soma = (soma + matriz[i][j])
  lista.append(soma)
  
cont = 0

for i in range (0,n,1):
  for j in range (0,n,1):
    if (lista[i] - matriz[i][j] + (lista[((len(lista)) // 2) + i])-matriz[i][j]) > cont:
      cont = (lista[i] - matriz[i][j] + (lista[((len(lista)) // 2) + i])-matriz[i][j])
    

print (cont)
  
