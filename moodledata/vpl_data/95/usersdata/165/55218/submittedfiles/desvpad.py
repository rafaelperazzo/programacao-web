# -*- coding: utf-8 -*-
import math
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    
    media=soma/len(lista)
    return(media)
    
def desvio(lista):
    x=media(lista)
    soma=0
    for i in range(0,len(lista),1):
        

