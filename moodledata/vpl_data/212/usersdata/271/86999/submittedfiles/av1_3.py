# -*- coding: utf-8 -*-
import math
#ENTRADA
z = int(input('Digite o valor de z : '))
#PROCESSAMENTO
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
print(primo(z))
            
        
