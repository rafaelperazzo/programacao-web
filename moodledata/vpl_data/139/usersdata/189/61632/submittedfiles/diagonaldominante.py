
import numpy as np

def soma(a):
    b=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for l in range(0,a.shape[1],1):
            if i!=l:
                soma=soma+a[i,l]
            b.append(soma)
        return (b)

def diagonal (a,b):
    for i in range (0,a.shape[0],1):
        for l in range(0,a.shape[1],1):
            if i==l:
                if a[i,l]<b[i]:
                    return False
    return True

n=int(input('Matriz:'))
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for l in range(0,a.shape[1],1):
            a[i,l]=int(input('valor:'))
b=soma(a)

if diagonal(a,b):
    print('SIM')
else:
    print('NÃO')