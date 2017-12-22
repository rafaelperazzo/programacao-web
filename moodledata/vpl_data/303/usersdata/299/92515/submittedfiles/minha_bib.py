# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
def sorteio(x,y):
    import random 
    sort=random.randint(1,2)
    if sort==1:
        return('Computador')
    else:
        return('Usuário')
def mostrar_tabuleiro (l,c):
    linha=[0,1,2]
    tabuleiro=[linha]*3
    tabuleiro[l][c]=
    return('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])

