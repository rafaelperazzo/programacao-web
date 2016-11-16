# -*- coding: utf-8 -*-
from __future__ import division
def qiguais(a,b):
    cont=0
    for i in range(0, len(a),1):
        for j in range(0, len(b),1):
            if a[i]==a[j]:
                cont=cont+1
    return cont
