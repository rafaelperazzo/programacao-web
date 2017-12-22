# -*- coding: utf-8 -*-
n = int(input("Digite a dimensão da matriz: "))
matriz = []
for i in range (0,n,1):
    lista=[]
    for j in range (0,n,1):
        lista.append(int(input("Digite o custo de transporte: ")))
    matriz.append(lista)
c = int(input("Digite a quantidade de cidades do seu itinerário: "))
while not c>=2:
    c = int(input("Dígito inválido! Digite a quantidade de cidades do seu itinerário: "))
lista1 = []
for i in range (0,c,1):
    lista1.append(int(input("Digite os elementos do seu intinerário: ")))
i = 0
for i in range (0,c,1):
    if not lista1[i]>=0 and lista[i]<= c-1:
       i += 1 
lista1.append(int(input("Digite os elementos do seu intinerário: ")))   
 
    
    