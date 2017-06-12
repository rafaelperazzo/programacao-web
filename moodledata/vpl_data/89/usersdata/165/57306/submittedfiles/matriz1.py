# -*- coding: utf-8 -*-

def menorlinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return(i)

def menorcoluna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return(j)
                
def maiorlinha(a):
    for i in range(a.shape[0]-1,-1,-1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return(i)
                
def maiorcoluna(a):
    for j in range(a.shape[1]-1,-1,-1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return(j)
                
linhas=int(input('digite a quantidade de linhas:'))
colunas=int(input('digite a quantidade de colunas:'))
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite um valor:'))
        
        
x=menorlinha(a)
y=maiorlinha(a)
z=menorcoluna(a)
w=maiorcoluna(a)

print(a[x:y+1,z:w+1])
        


