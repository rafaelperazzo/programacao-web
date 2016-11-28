# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somadiagonal1(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma+=a[i,i]
    return soma

def somadiagonal2(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma+=a[i,a.shape[0]-i-1]
    return soma

def somalinhas(a):
    s=[]
    for i in range(0,a.shape[0],1):
        s[i]=0
        for i in range(0,a.shape[1],1):
            