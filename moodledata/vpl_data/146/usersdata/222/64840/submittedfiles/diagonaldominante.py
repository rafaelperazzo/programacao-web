# -*- coding: utf-8 -*-
def def(m,n):
    val_det=1
    for i in range(n):
        if m[i][i]==0:
            soma=0
        else:
            soma=m[j][i] / m[i][i]
        for k in range(i+1,n):