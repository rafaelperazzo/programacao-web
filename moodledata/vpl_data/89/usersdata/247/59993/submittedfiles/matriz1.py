import numpy as np
linha=int(input('d: '))
coluna=int(input('b: '))
a=np.zeros(linha,coluna)
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input(' ')
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
        for i in range(0,a.shape[1],1):
            if a[i,j]==1:
                return(j)
b=menorlinha(a)
c=maiorlinha(a)
d=menorcoluna(a)
e=maiorcoluna(a)
print(a[bc+1,de+1])