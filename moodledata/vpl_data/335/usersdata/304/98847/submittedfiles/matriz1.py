# -*- coding: utf-8 -*-
import numpy as np

def recorte(matriz):
    
    linha = len(matriz)
    coluna = len(matriz[0])
    
    i_linha = linha
    i_coluna = coluna
    f_linha = 0
    f_coluna = 0
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] == 1:
                if i < i_linha: 
                    i_linha = i
                if j < i_coluna:
                    i_coluna = j
                if i + 1 > f_linha:
                    f_linha = i + 1
                if j + 1 > f_coluna:
                    f_coluna = j + 1

    a = []
    for i in range(i_linha,f_linha):
        l = []
        for j in range(i_coluna,f_coluna):
            l.append(matriz[i][j])
        a.append(linha)
    return(a)
