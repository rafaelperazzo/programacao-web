# -*- coding: utf-8 -*-
def verifica(a):
    aux=()
    for i in range(len(a)):
        soma=0
        soma2=0
        for j in range(len(a[i])):
            soma=soma+a[i][j]
            soma2=soma2+a[j][i]
        aux.append(soma)
        aux.append(soma2)
    soma=0
    soma2=0
    c=1
    for i in range(len(a)):
        soma=soma+a[i][i]
        soma2=soma2+a[i][len(a)-c]
        c=c+1
    aux.append(soma)
    aux.append(soma2)
    for i in range(len(aux)):
        if aux[i]!=aux[1]:
            return False
    return True
n=int(input('numero de linhas e colunas:'))
a=np.zeros((n,n))
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        a[i,j]=int(input('numero:'))
cont=0
if soma1(
    print('S')
else:
    print('N')
    

