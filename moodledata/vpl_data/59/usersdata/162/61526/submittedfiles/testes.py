import numpy as np
def somalinhas(a):
    b=[]
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        b.append(soma)
def somacolunas(a):
    c=[]
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        c.append(soma)
def diagonal(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return (soma)
def diagonalsec(a):
    soma=0
    for i in range(a.shape[0]-1,-1,-1):
        soma=soma+a[i,i]
    return (soma)
def magico(a):
    x=somalinhas(a)
    y=somacolunas(a)
    d=diagonal(a)
    e=diagonalsec(a)
    for i in range(0,len(x),1):
        if x[i] in not y:
            return False
    for i in range(0,len(y),1):
        if y[i] in x:
            if d==y[0] and e==y[0]:
                return True
linhas=int(input('LInhas: '))
colunas=int(input('colunas: '))
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('valores: '))
if magico(a):
    print('S')
else:
    print('N')