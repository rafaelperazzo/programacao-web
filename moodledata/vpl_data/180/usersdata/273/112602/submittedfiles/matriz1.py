# -*- coding: utf-8 -*-
def primeira_linha (a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return(i)
                

def primeira_coluna (a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return(j)

def ultima_linha (a):
    for i in range (a.shape[0]-1,-1,-1):
        for j in range(a.shape[1]-1,-1,-1):
            if a[i,j]==1:
                return(i)


def ultima_coluna (a):
    for j in range (a.shape[1]-1,-1,-1):
        for i in range(a.shape[0]-1,-1,-1):
            if a[i,j]==1:
                return(j)
                

linhas=int(input('Digite a quantidade de linhas: '))
colunas=int(input('Digite a quantidade de colunas: '))
a=np.zeros((linhas,colunas))

for i in range (0,a.shape[1],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Digite o valor: '))

menor_linha=primeira_linha(a)
maior_linha=ultima_linha(a)
menor_coluna=primeira_coluna(a)
maior_coluna=ultima_coluna(a)

b=a[menor_linha:maior_linhs+1,menor_coluna:maior_coluna+1]
print(b)


