# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
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

def verificar_vitoria(x):
    cont=0
    for i in range(1,3,1):
            for j in range(1,3,1):
                if x[i-1][j-1]==x[i][j]==" ":
                    cont+=0
    #analise linha
    for i in range(0,3,1):
        for j in range(1,3,1):
            if x[i][j-1]==x[i][j]:
                cont+=1
            elif x[0][0]==x[1][1] and x[1][1]==x[2][2]:
                cont+=1
            elif x[2][0]==x[1][1] and x[1][1]==x[0][2]:
                cont+=1
            else:
                cont+=0
    #Vitoria na coluna
    for j in range(0,3,1):
        for i in range(1,3,1):
            if x[i-1][j]==x[i][j]:
                cont+=1
            elif x[0][0]==x[1][1] and x[1][1]==x[2][2]:
                cont+=1
            elif x[2][0]==x[1][1] and x[1][1]==x[0][2]:
                cont+=1
            else:
                cont+=0
    if cont==0:
        return False
    else:
        return True

'''def maquinainteligente(x):
    from minha_bib import sorteio2
    #linhas
    #primeira
    if x[0][0]==x[0][2]:
        return('01')
    elif x[0][1]==x[0][2]:
        return('00')
    elif x[0][0]==x[0][1]:
        return('02')
    #segunda
    elif x[1][0]==x[1][1]:
        return('12')
    elif x[1][1]==x[1][2]:
        return('10')
    elif x[1][0]==x[1][2]:
        return('11')
    #terceira
    elif x[2][0]==x[2][1]:
        return('22')
    elif x[2][1]==x[2][2]:
        return('20')
    elif x[2][0]==x[2][2]:
        return('21')
    #colunas
    #primeira
    elif x[0][0]==x[1][0]:
        return('20')
    elif x[1][0]==x[2][0]:
        return('00')
    elif x[0][0]==x[2][0]:
        return('10')
    #segunda
    elif x[0][1]==x[1][1]:
        return('21')
    elif x[1][1]==x[2][1]:
        return('01')
    elif x[0][1]==x[2][1]:
        return('11')
    #terceira
    elif x[0][2]==x[1][2]:
        return('22')
    elif x[1][2]==x[2][2]:
        return('02')
    elif x[0][2]==x[2][2]:
        return('12')
    #diagonal
    elif x[0][0]==x[1][1]:
        return('22')
    elif x[1][1]==x[2][2]:
        return('00')
    elif x[0][0]==x[2][2]:
        return('11')
    #segunda
    elif x[2][0]==x[1][1]:
        return('02')
    elif x[1][1]==x[0][2]:
        return('20')
    elif x[2][0]==x[0][2]:
        return('11')
    else:
        retur(str(sorteio2(0,2))+str(sorteio2(0,2)))'''
def mostrar_tabuleiro(tabuleiro):
    return print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
                
def maquinainteligente(x):
    for i in range(0,3,1):
        for j in range(1,3,1):
            if x[i-1]==[i]:
                return i+1
            elif x[i-1]==[i+1]:
                return i
            elif x[i]==x[i+1]:
                return i-1
    