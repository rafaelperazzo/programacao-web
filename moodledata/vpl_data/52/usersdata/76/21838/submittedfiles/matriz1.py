# -*- coding: utf-8 -*-
from __future__ import division

def menorColuna(a):
    for j in range(0,a.shape(1),1):
        for i in range(0,a.shape(0),1):
            if a[i,j] == 1:
                return j

def maiorColuna(a):
    for j in range(0,a.shape(1),1):
        for i in range(0,a.shape(0),1):
            if a[i,j] == 1:
                CD = j
    return CD
    
def menorLinha(a):
    for i in range(0,a.shape(0),1):
        for j in range(0,a.shape(1),1):
            if a[i,j] == 1:
                return i

def maiorLinha(a):
    for i in range(0,a.shape(0),1):
        for j in range(0,a.shape(1),1):
            if a[i,j] == 1:
                LB = i
    return LB

