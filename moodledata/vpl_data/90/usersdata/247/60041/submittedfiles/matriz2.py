import numpy as np
x=int(input('d: '))
a=np.zeros((x,x))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('s: '))

def magico(a):
    soma1=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma1=soma1+a[i,j]
    return soma1
if soma1%(x**2+2)==0:
    print('S')
else:
    print('N')
    
