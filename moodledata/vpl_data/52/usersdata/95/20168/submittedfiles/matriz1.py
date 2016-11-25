# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def menor_coluna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return j

def maior_coluna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                CD=j
    return CD

def menor_linha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shpe[1],1):
            if a[i,j]==1:
                return i

def maior_linha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                LB=i
    return LB
    

