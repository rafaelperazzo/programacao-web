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
    cont=0
    for i in range(1,3,1):
            for j in range(1,3,1):
                if x[i-1][j-1]==x[i][j]==" " or x[j-1][i-1]==x[j][i]==" ":
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

 
    