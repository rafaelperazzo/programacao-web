# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de listas: "))
n=int(input("Digite a quantidade de elementos para a sua lista: "))
matriz=[]
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input("Digite o elemento da sua lista: ")))
    matriz.append(linha)

media=[]
for i in range(0,m,1):
    media.append(sum(matriz[i])/n)

somatorio=[]
so=0
for i in range(0,m,1):
    so=0
    for j in range(0,n,1):
        so=so+(matriz[i][j]-media[i])**2
    somatorio.append(so)
    

desvio=[]
for i in range(0,m,1):
    s=0
    s=(1/(n-1)*somatorio[i])**(1/2)
    desvio.append(s)
for i in range(0,m,1):
    print("%.2f"%media[i])
    print("%.2f"%desvio[i])

