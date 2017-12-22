# -*- coding: utf-8 -*-

mt=[]
n=int(input("Digite a dimensão da matriz:"))

for i in range (n,0,-1):
    lista=[]
    for j in range (n,0,-1):
        lista.append(int(input("Digite um elemento para sua matriz:")))
    mt.append(lista)

print(mt)
