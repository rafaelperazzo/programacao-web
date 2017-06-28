# -*- coding: utf-8 -*-
def melinha (matriz):
    for i in range (0,matriz.shape[0],1):
        for i in range (0,matriz.shape[1],1):
            if matriz[i,j]==1:
                return(i)
    

