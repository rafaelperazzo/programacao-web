# -*- coding: utf-8 -*-
def menorLinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return i
def menorColuna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return j
def maiorLinha(a):
    for i in range(a.shape[0]-1,-1,-1):
        for j in range(a.shape[1]-1,-1,-1):
            if a[i,j]==1:
                return i
def maiorColuna(a):
    for j in range(a.shape[1]-1,-1,-1):
        for i in range(a.shape[0]-1,-1,-1):
            if a[i,j]==1:
                return j
linhas=int(input('Digite a quantidade de linhas'))
colunas=int(input('Digite a quantidade de colunas'))
a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for i in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite um valor para a lista'))
i_i=menorLinha(a)
i_f=maiorLinha(a)
j_i=menorColuna(a)
j_f=maiorColuna(a)
print(a[i_i:i_f,j_i:j_f])

