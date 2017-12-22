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

"""def verificar_vitoria(x):
    #Vitoria na linha
    x[0][0] x[0][1] x[0][2]
    x[1][0] x[1][1] x[1][2]
    x[2][0] x[2][1] x[2][2]
    #Vitoria na coluna
    x[0][0] x[0][0] x[0][0]
    x[0][1] x[1][1] x[2][1]
    x[0][2] x[1][2] x[2][2]
    #Vitoria na diagonal
    x[0][0] x[1][1] x[2][2]
    x[2][0] x[1][1] x[0][2]"""
 