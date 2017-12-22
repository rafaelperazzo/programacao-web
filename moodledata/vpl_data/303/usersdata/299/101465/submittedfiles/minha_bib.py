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
    elif sort==2:
        return(2)
    else:
        return(1)
def verificar_vitoria(x):
    cont=0
    #analise linha
    if x[0][0]==x[0][1] and x[0][1]==x[0][2] and x[0][1]!=' ':
        cont+=1
    elif x[1][0]==x[1][1] and x[1][1]==x[1][2] and x[1][1]!=' ':
        cont+=1
    elif x[2][0]==x[2][1] and x[2][1]==x[2][2] and x[2][1]!=' ':
        cont+=1
    #Vitoria na coluna
    elif x[0][0]==x[1][0] and x[1][0]==x[2][0] and x[0][0]!=' ':
        cont+=1
    elif x[0][1]==x[1][1] and x[1][1]==x[2][1] and x[2][1]!=' ':
        cont+=1
    elif x[0][2]==x[1][2] and x[1][2]==x[2][2] and x[2][2]!=' ':
        cont+=1
    #vitoria diagonal
    elif x[0][0]==x[1][1] and x[1][1]==x[2][2] and x[1][1]!=' ':
        cont+=1
    elif x[2][0]==x[1][1] and x[1][1]==x[0][2] and x[1][1]!=' ':
        cont+=1
    if cont==0:
        return False
    else:
        return True
def mostrar_tabuleiro(tabuleiro):
    return print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
def maquinainteligente(x):
    from minha_bib import sorteio2
    #analise linha
    #primeira
    if x[0][0]!=x[0][1] and x[0][1]==x[0][2] and x[0][0]==' ':
        return '00'
    elif x[0][0]==x[0][1] and x[0][1]!=x[0][2] and x[0][2]==' ':
        return '02'
    elif x[0][0]==x[0][2] and x[0][1]!=x[0][2] and x[0][1]==' ':
        return '01'
    #segunda
    elif x[1][0]!=x[1][1] and x[1][1]==x[1][2] and x[1][0]==' ':
        return '10'
    elif x[1][0]==x[1][1] and x[1][1]!=x[1][2] and x[1][2]==' ':
        return '12'
    elif x[1][0]==x[1][2] and x[1][1]!=x[1][2] and x[1][1]==' ':
        return '11'
    #terceira
    elif x[2][0]!=x[2][1] and x[2][1]==x[2][2] and x[2][0]==' ':
        return '20'
    elif x[2][0]==x[2][1] and x[2][1]!=x[2][2] and x[2][2]==' ':
        return '22'
    elif x[2][0]==x[2][2] and x[2][1]!=x[2][2] and x[2][1]==' ':
        return '21'
    
    #coluna
    #primeira
    elif x[0][0]!=x[1][0] and x[1][0]==x[2][0] and x[0][0]==' ':
        return '00'
    elif x[0][0]==x[1][0] and x[1][0]!=x[2][0] and x[2][0]==' ':
        return '20'
    elif x[0][0]==x[2][0] and x[1][0]!=x[2][0] and x[1][0]==' ':
        return '10'
    #segunda
    elif x[0][1]!=x[1][1] and x[1][1]==x[2][1] and x[0][1]==' ':
        return '01'
    elif x[0][1]==x[1][1] and x[1][1]!=x[2][1] and x[2][1]==' ':
        return '21'
    elif x[0][1]==x[2][1] and x[1][1]!=x[2][1] and x[1][1]==' ':
        return '11'
    #terceira
    elif x[0][2]!=x[1][2] and x[1][2]==x[2][2] and x[0][2]==' ':
        return '02'
    elif x[0][2]==x[1][2] and x[1][2]!=x[2][2] and x[2][2]==' ':
        return '22'
    elif x[0][2]==x[2][2] and x[1][2]!=x[2][2] and x[1][2]==' ':
        return '12'
    #vitoria diagonal
    elif x[0][0]!=x[1][1] and x[1][1]==x[2][2] and x[0][0]==' ':
        return '00'
    elif x[0][0]==x[1][1] and x[1][1]!=x[2][2] and x[2][2]==' ':
        return '22'
    elif x[0][0]==x[2][2] and x[1][1]!=x[2][2] and x[1][1]==' ':
        return '11'
    elif x[2][0]!=x[1][1] and x[1][1]==x[0][2] and x[2][0]==' ':
        return '20'
    elif x[2][0]==x[1][1] and x[1][1]!=x[0][2] and x[0][2]==' ':
        return '02'
    elif x[2][0]==x[0][2] and x[1][1]!=x[0][2] and x[1][1]==' ':
        return '11'
    else:
        return(str(sorteio2(0,2))+str(sorteio2(0,2)))
def maquinainteligente2(x):
    #analise linha
    #primeira
    if x[0][0]!=x[0][1] and x[0][1]==x[0][2] and x[0][0]==' ':
        return '00'
    elif x[0][0]==x[0][1] and x[0][1]!=x[0][2] and x[0][2]==' ':
        return '02'
    elif x[0][0]==x[0][2] and x[0][1]!=x[0][2] and x[0][1]==' ':
        return '01'
    #segunda
    elif x[1][0]!=x[1][1] and x[1][1]==x[1][2] and x[1][0]==' ':
        return '10'
    elif x[1][0]==x[1][1] and x[1][1]!=x[1][2] and x[1][2]==' ':
        return '12'
    elif x[1][0]==x[1][2] and x[1][1]!=x[1][2] and x[1][1]==' ':
        return '11'
    #terceira
    elif x[2][0]!=x[2][1] and x[2][1]==x[2][2] and x[2][0]==' ':
        return '20'
    elif x[2][0]==x[2][1] and x[2][1]!=x[2][2] and x[2][2]==' ':
        return '22'
    elif x[2][0]==x[2][2] and x[2][1]!=x[2][2] and x[2][1]==' ':
        return '21'
    
    #coluna
    #primeira
    elif x[0][0]!=x[1][0] and x[1][0]==x[2][0] and x[0][0]==' ':
        return '00'
    elif x[0][0]==x[1][0] and x[1][0]!=x[2][0] and x[2][0]==' ':
        return '20'
    elif x[0][0]==x[2][0] and x[1][0]!=x[2][0] and x[1][0]==' ':
        return '10'
    #segunda
    elif x[0][1]!=x[1][1] and x[1][1]==x[2][1] and x[0][1]==' ':
        return '01'
    elif x[0][1]==x[1][1] and x[1][1]!=x[2][1] and x[2][1]==' ':
        return '21'
    elif x[0][1]==x[2][1] and x[1][1]!=x[2][1] and x[1][1]==' ':
        return '11'
    #terceira
    elif x[0][2]!=x[1][2] and x[1][2]==x[2][2] and x[0][2]==' ':
        return '02'
    elif x[0][2]==x[1][2] and x[1][2]!=x[2][2] and x[2][2]==' ':
        return '22'
    elif x[0][2]==x[2][2] and x[1][2]!=x[2][2] and x[1][2]==' ':
        return '12'
    #vitoria diagonal
    elif x[0][0]!=x[1][1] and x[1][1]==x[2][2] and x[0][0]==' ':
        return '00'
    elif x[0][0]==x[1][1] and x[1][1]!=x[2][2] and x[2][2]==' ':
        return '22'
    elif x[0][0]==x[2][2] and x[1][1]!=x[2][2] and x[1][1]==' ':
        return '11'
    elif x[2][0]!=x[1][1] and x[1][1]==x[0][2] and x[2][0]==' ':
        return '20'
    elif x[2][0]==x[1][1] and x[1][1]!=x[0][2] and x[0][2]==' ':
        return '02'
    elif x[2][0]==x[0][2] and x[1][1]!=x[0][2] and x[1][1]==' ':
        return '11'
    else:
        if x[1][1]==' ':
            return '11'
        #diagonal principal
        elif x[0][0]==x[1][1] and x[0][1]==' ':
            return '01'
        elif x[1][1]==x[2][2] and x[2][1]==' ':
            return '21'
        #diagonal secundária
        elif x[2][0]==x[1][1] and x[2][1]==' ':
            return '21'
        elif x[0][2]==x[1][1] and x[0][1]==' ':
            return '01'