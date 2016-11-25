# -*- coding: utf-8 -*-
from __future__ import division
import math

#SUPONDO QUE AS FUNÇÕES ESTAO ESCRITAS AQUI!!

def quadradomagico(a):
    
    sd1 = somaDiagonal1(a)
    sd2 = somaDiagonal2(a)
    
    somaL = somaLinhas(a)
    somaC = somaColunas(a)
    
    cont = 0
    for i in range(0,len(somaL),1):
        if sd1==sd2==somaL[i]==somaC[i]:
            cont = cont + 1
    
    if cont == len(somaL):
        return True
    else:
        return False



    
    
    
    