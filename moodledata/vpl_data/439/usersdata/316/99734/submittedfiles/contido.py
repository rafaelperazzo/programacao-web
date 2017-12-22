# -*- coding: utf-8 -*-
def fim(lista):
    i=1
    qa=input('Digite o número de elementos da primeira lista:')
    while i<=qa:
        x=int(input('digite um numero:'))
        i=i+1
    i=1
    qb=input('Digite o número de elementos da segunda lista:')
    while i<=qb:
        y=int(input('digite um numero:'))
        i=i+1
    
    if qa>=qb:
        w=qa-x+y
    else:
        w=qb-x+y
    return w




    