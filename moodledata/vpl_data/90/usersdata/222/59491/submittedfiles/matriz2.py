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
    soam=0
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
n=int(input('n:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[0],1):
if verifica(a):
    print('S')
else:
    print('N')
    

