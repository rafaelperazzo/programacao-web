# -*- coding: utf-8 -*-
from __future__ import division

def m_mov(lista,altura_desbloqueio):    #m_mov=minimo de movimentos
    a=max(lista)-altura_desbloqueio
    b=altura_desbloqueio-min(lista)
    mov_min=a+b
    return int(mov_min)
n=input("Entre com a quantidade de pinos: ")
m=input("Entre com a altura de desbloqueio: ")

l=[]
while n>0:
    l.append(input("Entre com a altura do pino: "))
    n=n-1

print "Minimo de movimentos:",m_mov(l,m)