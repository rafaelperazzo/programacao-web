# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

def algarismos(n):
    alg=1
    while (n//10)>0:
        n=n//10
        alg=alg+1
    return alg
    
def fatorial(n):
    f=1
    for i in range(1,n+1,1):
        f=f*i
    return f
    
def verificar_vitoria(x):
    venc=False
    vitorias=[['X', 'X', 'X'], ['O', 'O', 'O']]
    
    #analisando linhas
    for i in range (0, 3, 1):
        if x[i] in vitorias:
            venc=True
            break
        if not x[i] in vitorias:
            continue
    
    #analisando colunas    
    for i in range (0, 3, 1):
        coluna=[]
        for j in range (0, 3, 1):
            coluna.append(x[j][i])
        if coluna in vitorias:
            venc=True
            break
        if not coluna in vitorias:
            continue
    
    #analisando diagonais
    diagonal1=[]
    for i in range (0, 3, 1):
        diagonal1.append(x[i][i])
    if diagonal1 in vitorias:
        venc=True
        break
    if not diagonal1 in vitorias:
        continue
    
    diagonal2=[x[0][2], x[1][1], x[2][0]]
    if diagonal2 in vitorias:
        venc=True
        break
    
    return venc