
import numpy as np

def soma(a):
    c=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for l in range(0,a.shape[1],1):
            if i!=l:
                soma=soma+a[i,l]
            c.append(soma)
        return (c)

def diagonal (a,b):
    for i in range (0,a.shape[0],1):
        for l in range(0,a.shape[1],1):
            if i==l:
                if a[i,l]<b[i]:
                    return False
    return True

n=in(input('Matriz:'))
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for l in range(0,a.shape[1],1):
            a[a,l]=int(input('valor:'))
b=soma(a)

if diagonal(a,b):
    print('sim')
else:
    print(´não')