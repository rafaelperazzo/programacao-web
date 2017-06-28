import numpy as np
def somalinhas(a):
    b=[]
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(,a.shape[1],1):
            soma=soma+a[i,j]
        b.append(soma)
def somacolunas(a):
    c=[]
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(,a.shape[1],1):
            soma=soma+a[i,j]
        c.append(soma)
def diagonal(a):
    soma=0
    for i in range(0,ashape[0],1):
        soma=soma+a[i,i]
    return (soma)
def diagonalsec(a):
    soma=0
    for i in range(ashape[0]-1,-1,-1):
        soma=soma+a[i,i]
    return (soma)
def magico(a):
    x=somalinhas(a)
    y=somacolunas(a)
    d=diagonal(a)
    e=diagonalsec(a)
    if x in y:
        if d==x[0]:
            return True
    else:
        return False
linhas=int(input('LInhas: '))
colunas=int(input('colunas: '))
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shhape[1],1):
        a[i,j]=int(input('valores: '))
if magico(a):
    print('S')
else:
    print('N')