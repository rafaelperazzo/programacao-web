# -*- coding: utf-8 -*-
import numpy as np
n=int(input('ordem: '))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('elemento: '))
def estritamentedominante(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=0
            if i==j:
                maior=a[i,j]
            else:
                soma=soma+a[i,j]
        if maior<soma:
            return False
        else:
            return True
if estritamentedominante(a):
    print('SIM')
else:
    print('NAO')