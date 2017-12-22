# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
def sorteio(x,y):
    import random 
    sort=random.randint(0,2)
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
                break
    if x[0][0]==x[0][1] and x[0][1]==x[0][2]:
        return(True)
    elif x[1][0]==x[1][1] and x[1][1]==x[1][2]:
        return(True)
    elif x[2][0]==x[2][1] and x[2][1]==x[2][2]:
        return(True)
    #Vitoria na coluna
    elif x[0][0]==x[1][0] and x[1][0]==x[2][0]:
        return(True)
    elif x[0][1]==x[1][1] and x[1][1]==x[2][1]:
        return(True)
    elif x[0][2]==x[1][2] and x[1][2]==x[2][2]:
        return(True)
    #Vitoria na diagonal
    elif x[0][0]==x[1][1] and x[1][1]==x[2][2]:
        return(True)
    elif x[2][0]==x[1][1] and x[1][1]==x[0][2]:
        return(True)
    else:
        return(False)
 