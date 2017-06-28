import numpy as np
def diagonal(a):
    v=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                v.append(a[i,j])
        return (v)
def soma(a):
    b=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            if i!=j:
                soma=soma+a[i,j]
            b.append(soma)
    return (b)
def estritamente(a):
    x=diagonal(a)
    y=soma(a)
    for i in range(0,len(x),1):
        if x[i]<y[i]:
            return False
    retuurn True
linhas=int(input('l:    ' ))
colunas=int(input('c:    ' ))
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('valores '))
if estritamente(a):
    print('s')
else:
    print('n')