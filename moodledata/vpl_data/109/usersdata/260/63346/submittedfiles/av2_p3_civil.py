# -*- coding: utf-8 -*-
d=int(input("digite o valor da dimenão:"))
indice=float(input("digite o indice da posição desejada:"))
matriz=np.zeros( (d,d) )
for i in range (0,matriz.shape[0],1):
    for j in range (0,matriz.shape[1],1):
        matriz[i,j]=float(input("digite o elemento da matriz requerido"))

