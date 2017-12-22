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
    sort=random.randint(x,y)
    if sort==0:
        return(0)
    if sort==2:
        return(2)
    else:
        return(1)
def verificar_vitoria(x):
    #Vitoria na linha
    for i in range(1,3,1):
            for j in range(1,3,1):
                if x[i-1][j-1]==x[i][j]==" ":
                    return(False)
    if x[0][0]==x[0][1] and x[0][1]==x[0][2]:
        return True
    elif x[1][0]==x[1][1] and x[1][1]==x[1][2]:
        return True
    elif x[2][0]==x[2][1] and x[2][1]==x[2][2]:
        return True
    #Vitoria na coluna
    elif x[0][0]==x[1][0] and x[1][0]==x[2][0]:
        return True
    elif x[0][1]==x[1][1] and x[1][1]==x[2][1]:
        return True
    elif x[0][2]==x[1][2] and x[1][2]==x[2][2]:
        return True
    #Vitoria na diagonal
    elif x[0][0]==x[1][1] and x[1][1]==x[2][2]:
        return True
    elif x[2][0]==x[1][1] and x[1][1]==x[0][2]:
        return True
    else:
        return(False)
def jogadauser(nome1,tabuleiro,jogada,s1):
    from jogoDaVelha_BIB import verificar_vitoria
    from jogoDaVelha_BIB import sorteio
    from jogoDaVelha_BIB import sorteio2
    import time
    i=jogada[0]
    j=jogada[1]
    i=int(i)
    j=int(j)
    while tabuleiro[i][j]!=" ":
        return 'Jogada inválida'
        jogada=str(input('Qual a sua jogada?'))
        i=jogada[0]
        j=jogada[1]
    i=int(i)
    j=int(j)
    tabuleiro[i][j]=s1
    return print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])

def jogadapc(tabuleiro,s2):
    from jogoDaVelha_BIB import verificar_vitoria
    from jogoDaVelha_BIB import sorteio2
    import time
    time.sleep(2)
    i=sorteio2(0,2)
    j=sorteio2(0,2)
    while tabuleiro[i][j]!=" ":
        i=sorteio2(0,2)
        j=sorteio2(0,2)
    tabuleiro[i][j]=s2
    return print('minha vez\n ',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
    