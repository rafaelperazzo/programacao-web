# -*- coding: utf-8 -*-
import math
#ENTRADA
a = int(input('Digite o valor de a : '))
b = int(input('Digite o valor de b : '))
c = int(input('Digite o valor de c : '))
#PROCESSAMENTO
def primo(x) :
    cont = 0
    n = x
    for x in range (2,x,1) :
        if ((n%x)==0) :
            cont = cont +1
        if (cont!=0) :
            return(True)
        else :
            return(False)
        
