# -*- coding: utf-8 -*-
import math
#ENTRADA
z = int(input('Digite o valor de z : '))
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
print(primo(z))
            
        
