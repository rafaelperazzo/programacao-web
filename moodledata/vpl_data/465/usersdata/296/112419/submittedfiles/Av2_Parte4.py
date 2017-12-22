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
soma = matriz[(lista[0])][(lista[1])] + matriz[(lista[1])][(lista[2])] + matriz[(lista[2])][(lista[3])] + matriz[(lista[3])][(lista[4])] + matriz[(lista[4])][(lista[5])] + matriz[(lista[5])][(lista[6])] +matriz[(lista[6])][(lista[7])] + matriz[(lista[7])][(lista[8])]
