# -*- coding: utf-8 -*-
from __future__ import division
def qiguais(a,b):
    cont=0
    for i in range(0, len(a),1):
        for j in range(0, len(b),1):
            if a[i]==b[j]:
                cont=cont+1
    return cont
a=[1,2,3,4,5,6,7,8,9]
b=[2,4,7,9,45]
print(qiguais(a,b))