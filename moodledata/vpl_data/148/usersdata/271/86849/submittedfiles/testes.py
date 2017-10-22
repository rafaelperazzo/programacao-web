# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
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
        
    
    

