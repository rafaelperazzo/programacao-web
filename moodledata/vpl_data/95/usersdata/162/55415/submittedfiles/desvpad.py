# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('Digite n:'))
lista=[]
def media(lista):
    soma1=0
    for i in range(0,len(lista),1):
        soma1=soma1+lista[i]
    media=soma1/len(lista)
    return(media)
    