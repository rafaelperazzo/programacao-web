# -*- coding: utf-8 -*-
from __future__ import division

def qiguais(listax,listay):
    listax=[]
    listay=[]
    for i in range(0,len(listax),1):
        if listax[i] in listay:
            igual=igual+1
    return igual

y=[1,2,3,4,5,6,7,8,9,10]
x=[5,9,18,20]
print qiguais(x,y)