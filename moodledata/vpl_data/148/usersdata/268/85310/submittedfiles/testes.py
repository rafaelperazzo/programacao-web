# -*- coding: utf-8 -*-

def calcula_fatorial(y):
    fatorial=1
    while(y>0):
        fatorial=fatorial*y
        y=y-1
    return(fatorial)
n=int(input('hjhdfuroi : '))
print( calcula_fatorial(n))