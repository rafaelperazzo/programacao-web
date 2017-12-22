# -*- coding: utf-8 -*-

def verifica_linha_nula (matriz):
    listanulas=[]
    for i in range (0, len(matriz)-1, 1):
        cont=0
        for j in range (0, len(matriz[i])-1, 1):
            if matriz[i][j]==0:
                cont+=0
            if not matriz[i][j]==0:
                cont+=1
        if cont==0:
            listanulas.append(True)
        if not cont==0:
            listanulas.append(False)
    return listanulas
    
m=[[0, 0, 0], [1, 0, 1], [0, 0, 0]]
k= verifica_linha_nula (m)
print(k)
