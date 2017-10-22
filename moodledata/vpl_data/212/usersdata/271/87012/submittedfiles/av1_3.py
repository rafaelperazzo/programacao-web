# -*- coding: utf-8 -*-
import math
#ENTRADA
a = int(input('Digite o valor de a : '))
b = int(input('Digite o valor de b : '))
c = int(input('Digite o valor de c : '))
#FUNÇÃOPRIMO
def primo(x) :
    cont = 0
    div = 2
    while (div<x) :
        if (x%div==0) :
            cont = cont+1
        div = div+1
    if (cont!=0) :
        return(False)
    else :
        return(True)
#PROCESSAMENTO

            
        
