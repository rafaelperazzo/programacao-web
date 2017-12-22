# -*- coding: utf-8 -*-
n=int(input("Digite o número de linhas: "))
m=int(input("Digite o número de colunas: "))
matriz=[]
for i in range(0,n,1):
    linha=[]
    for i in range(0,m,1):
        linha.append(int(input("Digite o valor para a linha: ")))
    matriz.append(linha)
print(matriz)
matriz_recorte=[]
i_s=m-1
i_i=0
i_e=0
i_d=n-1

for i in range(0,m,1):
    encontrou_na_linha=False
    for j in range(0,n,1):
        if matriz[i][j]==1:
            encontrou_n_linha=True
            if j<i_e:
                i_e=j
            if j>i_d:
                i_d=1

            

