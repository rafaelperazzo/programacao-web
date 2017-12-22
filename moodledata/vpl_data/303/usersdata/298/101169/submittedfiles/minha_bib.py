# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO

def algarismos(n):
    alg=1
    while (n//10)>0:
        n=n//10
        alg=alg+1
    return alg
    
def fatorial(n):
    f=1
    for i in range(1,n+1,1):
        f=f*i
    return f
    
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
        for i in range(1,3,1):
            if x[i-1][j]==x[i][j]:
                return True
            elif x[0][0]==x[1][1] and x[1][1]==x[2][2]:
                return True
            elif x[2][0]==x[1][1] and x[1][1]==x[0][2]:
                return True
            else:
                return False
