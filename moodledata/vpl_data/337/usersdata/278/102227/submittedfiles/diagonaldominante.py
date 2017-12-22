# -*- coding: utf-8 -*-
n = int(input("Digite a ordem da matriz: "))
matriz = []
soma = []
for i in range (0,n,1):
    linha = []
    for i in range(0,n,1):
        linha.append(int(input("Digite o elememto%.d da matriz: " %(i+1))))
    matriz.append(linha)
for i in range (0,n,1):
    for j in range (0,n,1):
        if j>i:
            soma = soma + matriz[i][i] + matriz[i][j+1] + matriz[i][j+2]
            soma-=matriz[i][i]
            if matriz[i][i]>soma:
                c+=1
if c>0:
    print("SIM")
else:
    print("NAO")

