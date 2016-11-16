# -*- coding: utf-8 -*-
from __future__ import division

def qiguais(listax,listay):
    listax=[]
    listay=[]
    cont=0
    for i in range(0,len(listax),1):
        for j in range(0,len(listay),1):
            if listax[i]==listay[j]:
                cont=cont+1
    return cont

x=[1,2,3,4,5,6,7,8,9,10]
y=[5,9,18,20]
print qiguais(x,y)