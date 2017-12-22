# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def sorteio(x,y):
    import random 
    sort=random.randint(0,2)
    if sort==0:
        return(0)
    if sort==2:
        return(2)
def sorteio2(x,y):
    import random 
    sort=random.randint(0,2)
    if sort==0:
        return(0)
    if sort==2:
        return(2)
    else:
        return(1)
'''
def verificar_vitoria(x):
    cont=0
    #analise linha
    if x[0][0]==x[0][1] and x[0][1]==x[0][2]:
        cont+=1
    elif x[1][0]==x[1][1] and x[1][1]==x[1][2]:
        cont+=1
    elif x[2][0]==x[2][1] and x[2][1]==x[2][2]:
        cont+=1
    #Vitoria na coluna
    elif x[0][0]==x[1][0] and x[1][0]==x[2][0]:
        cont+=1
    elif x[0][1]==x[1][1] and x[1][1]==x[2][1]:
        cont+=1
    elif x[0][2]==x[1][2] and x[1][2]==x[2][2]:
        cont+=1
    #vitoria diagonal
    elif x[0][0]==x[1][1] and x[1][1]==x[2][2]:
        cont+=1
    elif x[2][0]==x[1][1] and x[1][1]==x[0][2]:
        cont+=1
    if cont==0:
        return False
    else:
        return True
        
#---------------------------------------------------------------#
'''
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

    