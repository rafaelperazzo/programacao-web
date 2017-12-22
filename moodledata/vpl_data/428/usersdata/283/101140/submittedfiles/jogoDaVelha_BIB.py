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

def verificar_vitoria(x):
    for i in range(0,3,1):
            for j in range(1,3,1):
                if x[i-1][j-1]==x[i][j]==" ":
                    return False
    #analise linha
    for i in range(0,3,1):
        for j in range(1,3,1):
            if x[i][j-1]==x[i][j]:
                return True
            elif x[0][0]==x[1][1] and x[1][1]==x[2][2]:
                return True
            elif x[2][0]==x[1][1] and x[1][1]==x[0][2]:
                return True
            else:
                return False
    #Vitoria na coluna
    for j in range(0,3,1):
        for i in range(0,2,1):
            if x[i][j]==x[i+1][j]:
                return True
            elif x[0][0]==x[1][1] and x[1][1]==x[2][2]:
                return True
            elif x[2][0]==x[1][1] and x[1][1]==x[0][2]:
                return True
            else:
                return False

 
    