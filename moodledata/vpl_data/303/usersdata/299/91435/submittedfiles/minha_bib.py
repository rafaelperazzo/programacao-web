# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
def sorteio(x,y):
    import random #1
    sort=random.randint(1,2)
    if sort==1:
        return('Computador')
    else:
        return('Usuário')
    
def matriz(linhas,colunas,valor):
    matriz=[]
    for i in range(linhas):
        linha=[]
        for j in range(colunas):
            linha.append(valor)
            matriz.append(linha)
    return (matriz)
            