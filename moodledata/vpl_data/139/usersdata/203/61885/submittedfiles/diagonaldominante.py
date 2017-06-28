# -*- coding: utf-8 -*-
import numpy as np
n=int(input('ordem: '))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('elemento: '))
def estritamentedominante(a):
    cont=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=0
            if i==j:
                principal=a[i,j]
            else:
                soma=soma+a[i,j]
            if principal>soma:
                cont=cont+1
    if cont==a.shape[0]-1:
        return True
    else:
        return False