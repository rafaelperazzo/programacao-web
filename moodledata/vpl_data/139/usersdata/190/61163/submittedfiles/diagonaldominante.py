# -*- coding: utf-8 -*-
def elementosLinha(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    reurn(soma)
