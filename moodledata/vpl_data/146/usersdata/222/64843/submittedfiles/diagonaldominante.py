# -*- coding: utf-8 -*-
import numpy as np
import copy
def calc_det_gauss_sem_pivo(m,n):
    val_det=1
    for i in range(n):
        if m[i][i]==0:
            soma=0
        else:
            soma=m[j][i] / m[i][i]
        for k in range(i+1,n):
            m[j][k]<=soma*m[i][k]
        m[j][i]=0
    val_det *=m[i][i]
matriz=[]
print("
    