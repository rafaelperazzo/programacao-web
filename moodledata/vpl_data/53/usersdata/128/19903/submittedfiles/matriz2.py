# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def qMagico(m):
    
    cont1=0
    
    for i in range (0,m.shape[0]-1,1):
        if sum(m[i,:])==sum(m[i+1,:]):
            cont1=cont1+1
            
    if cont2==m.shape[0]:
        l='sim'
    
    cont2=0
    
    for j in range (0,m.shape[1]-1,1):
        if sum(m[:,i])==sum(m[:,i]):
            cont2=cont2+1
            
    if cont2==m.shape[1]:
        c='sim'
        