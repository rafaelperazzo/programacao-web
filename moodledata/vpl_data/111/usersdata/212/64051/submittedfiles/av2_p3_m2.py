# -*- coding: utf-8 -*-
import numpy as np
x=int(input('Digite o numero de linhas:'))
b=np.zeros((x,x))
for i in range (0,b.shape[0],1):
    for j in range(0,b.shape[1],1):
        b=[i,j]-int(input('Digite um numero:'))

def somac(a):
    lista=[]
    for i ini range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+b[i,j]
