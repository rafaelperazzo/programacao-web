# -*- coding: utf-8 -*-
from __future__ import division

def min_mov(lista,alturadesbloqueio):  #min_mov=minimo movimentos
    a= (max(lista)-alturadesbloqueio
    b= 0
    mov_min=int(a+b)
    return (mov_min)

n=input("Entre com a quantidade de pinos: ")
m=input("Entre com a altura de desbloqueio: ")

l=[]
while n>0:
    l.append(input("Entre com a altura do pino: ")
    n=n-1
print min_mov(l,m)