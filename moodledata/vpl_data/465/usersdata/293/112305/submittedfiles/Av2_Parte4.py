# -*- coding: utf-8 -*-
n=int(input("Digite a ordem da matriz: "))
matriz=[]
for i in range(0,n,1):
    matriz_linha=[]
    for j in range(0,n,1):
        matriz_linha.append(int(input("Digite o elemento (%d,%d): "%(i+1,j+1))))
    matriz.append(matriz_linha)

c= int(input("Digite o número de cidades do intinerário: "))
while True:
    if c<2:
        c= int(input("Digite o número de cidades do intinerário: "))
    else:
        break
viagem=[]
for j in range(0,c,1):
    e=int(input("Digite o valor do intinerário: "))
    while True:
        if e<0 or e>=n-1:
            e=int(input("Digite o valor do intinerário: "))
        else:
            break
        
    viagem.append(e)

valor=0
i=0
for k in range(0,c-1,1):
    a=viagem[i]
    b=viagem[i+1]
    valor= valor+ matriz[a][b]
print(valor)
    
    
    
