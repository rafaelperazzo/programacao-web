# -*- coding: utf-8 -*-

n=(int(input()))
m=(int(input()))
matriz=[]

for i in range(0,n,1) :
  vetor=[]
  vetor.append(int(input()))
for i in range(0,m,1) :
    matriz.apppend(vetor)

   
      
matriz_recorte=[]
 
 indice_superior=m-1
 indice_inferior=0
 indice_esquerdo=0
 indice_direito=n-1

for i in range(0,m,1):
    encontrou_na_linha=False
    for j in range(0,n,1) :
        if matriz[i][j] == 1:
            encontrou_na_linha=True
            if 










