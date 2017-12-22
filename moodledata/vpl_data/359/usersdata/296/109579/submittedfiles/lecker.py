# -*- coding: utf-8 -*-
n = int(input("Digite a quantidade de elementos das listas: "))
lista1 = []
lista2 = []
for i in range (0,n,1):
    lista1.append(int(input("Digite um valor para a lista 1: ")))
for i in range (0,n,1):
    lista2.append(int(input("Digite um valor para a lista 2: ")))
cont1 = 0
for i in range (0,n-2,1):
    if lista1[i]<lista1[i+1]>lista1[i+2]:
        cont1 += 1
if lista1[0]>lista1[1] or lista1[n-1]>lista1[n-2]:
     cont1 += 1
if cont1 == 1:
    print ("S")
else:
    print ("N")
cont2 = 0
for i in range (0,n-2,1):
    if lista2[i]<lista2[i+1]>lista2[i+2]:
        cont2 += 1
if lista2[0]>lista2[1] or lista2[n-1]>lista2[n-2]:
     cont2 += 1
if cont2 == 1:
    print ("S")
else:
    print ("N")
    
    
        

