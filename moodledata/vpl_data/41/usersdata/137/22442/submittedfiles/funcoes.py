# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somaColunaA(a):
    b=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
            b.append (soma)
            return b
def somaLinhaA(a):
    b=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for i in range(0,m.shape[1],1):
            soma=soma+m[i,j]
            b.append (soma)
            return b

def matriz(a,o,d):
    T=n.zeros((len(a),len(a)))
    for i in range (0,d.shape[0],1):
        for j in range (0,d.shape[1],1):
            soma=0
            for k in range (0,d.shape[0],1):
                if i!=k:
                    soma=soma+a[k]*(1/d[i,k])
                if i!=j:
                    c[i,j]=(o[i])*a[j]*(1/(d[i,j]))**alfa)/soma
                
    return T
            

    