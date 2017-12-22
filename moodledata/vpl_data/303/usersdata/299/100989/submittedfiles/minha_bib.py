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
    #Vitoria na linha
    for i in range(1,3,1):
            for j in range(1,3,1):
                if x[i-1][j-1]==x[i][j]==" ":
                    return False
    #analise linha
    for i in range(1,3,1):
        for j in range(1,3,1):
            if x[i][j-1]==x[i][j]:
                cont+=0
            else:
                cont+=1
    #Vitoria na coluna
    for j in range(1,3,1):
        for i in range(1,3,1):
            if x[i-1][j]==x[i][j]:
                cont+=0
            else:
                cont+=1
    #Vitoria na diagonal
    if x[0][0]==x[1][1] and x[1][1]==x[2][2]:
        cont+=0
    elif x[2][0]==x[1][1] and x[1][1]==x[0][2]:
        cont+=0
    else:
        cont+=1
    if cont==0:
        return True
    else:
        return False





def maquinainteligente(x):
    from minha_bib import sorteio2
    #linhas
    #primeira
    for i in range(0,len(x)-1,1):
        for j in range(0,len(x)-1,1):
            
    if x[0][0]==x[0][2]:
        return '01'
    elif x[0][1]==x[0][2]:
        return '00'
    elif x[0][0]==x[0][1]:
        return '02'
    #segunda
    elif x[1][0]==x[1][1]:
        return '12'
    elif x[1][1]==x[1][2]:
        return '10'
    elif x[1][0]==x[1][2]:
        return'11'
    #terceira
    elif x[2][0]==x[2][1]:
        return '22'
    elif x[2][1]==x[2][2]:
        return '20'
    elif x[2][0]==x[2][2]:
        return '21'
    #colunas
    #primeira
    elif x[0][0]==x[1][0]:
        return '20'
    elif x[1][0]==x[2][0]:
        return '00'
    elif x[0][0]==x[2][0]:
        return '10'
    #segunda
    elif x[0][1]==x[1][1]:
        return '21'
    elif x[1][1]==x[2][1]:
        return '01'
    elif x[0][1]==x[2][1]:
        return '11'
    #terceira
    elif x[0][2]==x[1][2]:
        return '22'
    elif x[1][2]==x[2][2]:
        return '02'
    elif x[0][2]==x[2][2]:
        return '12'
    #diagonal
    elif x[0][0]==x[1][1]:
        return '22'
    elif x[1][1]==x[2][2]:
        return '00'
    elif x[0][0]==x[2][2]:
        return '11'
    #segunda
    elif x[2][0]==x[1][1]:
        return '02'
    elif x[1][1]==x[0][2]:
        return '20'
    elif x[2][0]==x[0][2]:
        return '11'

    
 