# -*- coding: utf-8 -*-
def media(lista):
    h=len(lista)
    soma=float(sum(lista))
    med=soma/h
    return med

def desv(lista):
    h=len(lista)
    soma=float(sum(lista))
    med=soma/h
    var=0
    for i in range (0, h, 1):
        var+=(lista[i]-med)**(2.0)
    s=((1.0/(h-1))*var)**(0.5)


    
