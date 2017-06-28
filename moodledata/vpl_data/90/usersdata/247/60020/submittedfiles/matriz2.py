import numpy as np
x=int(input('d: '))
a=np.zeros((x,x))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('s: '))

def magico(a):
    soma1=0
    soma2=0
    soma3=0
    for i in range(0,a.shape[0],1):
        soma1=a[i]+soma1
    for j in range(0,a.shape[1],1):
        soma2=a[j]+soma2
    if soma2==soma1:
        return True
    else:
        return False
if magico(a):
    print('S')
else:
    print('N')
    
