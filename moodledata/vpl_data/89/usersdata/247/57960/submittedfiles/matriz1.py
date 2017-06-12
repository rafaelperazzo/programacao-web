# -*- coding: utf-8 -*-
def maiorlista(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return(i)
            

