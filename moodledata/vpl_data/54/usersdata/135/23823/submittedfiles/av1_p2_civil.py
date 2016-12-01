# -*- coding: utf-8 -*-
from __future__ import division

def min_mov(lista,altura_desbloqueio):  #min_mov=minimo movimentos
    a=((max(lista))-altura_desbloqueio
    b=altura_desbloqueio-(min(lista))
    mov_min=int(a+b)
    return (mov_min)

n=input("Entre com a quantidade de pinos: ")
m=input("Entre com a altura de desbloqueio: ")

l=[]
while n>0:
    l.append(input("Entre com a altura do pino: ")
    n=n-1
print min_mov(l,m)