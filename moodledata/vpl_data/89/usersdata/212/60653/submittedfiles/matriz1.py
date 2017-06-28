# -*- coding: utf-8 -*-
def melinha (matriz):
    for i in range (0,matriz.shape[0],1):
        for i in range (0,matriz.shape[1],1):
            if matriz[i,j]==1:
                return(i)
def mecoluna (matriz):
    j=0
    while j<matriz.shap[1]:
        for i in range (0,matriz.shape[0],1):
            if matriz[i,j]==1:
                return(j)
        j=j+1
def malinha (matriz):
    i=matriz.shape[0]-1
    while i<=0:
        for j in range (0,matriz.shape[1],1):
            if matriz[i,j]==1:
                return(i)
        i=i-1
def malinha (matriz):
    j=matriz.shape[1]-1
    while i<=0:
        for i in range (0,matriz.shape[0],1):
            if matriz[i,j]==1:
                return(i)
        j=j-1
met