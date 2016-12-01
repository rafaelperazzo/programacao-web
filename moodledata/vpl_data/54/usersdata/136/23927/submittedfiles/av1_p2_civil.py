# -*- coding: utf-8 -*-
from __future__ import division

#Funções
def valorAbsoluto(x):
    if x<0:
        return x*(-1)
    else:
        return x

def pinoMaior(a):
    lista = a[0]
    for i in range(0, len(a), 1):
        if a[i]>lista:
            lista = a[i]
    return lista 

def pinoMenor(a):
    lista = a[0]
    for i in range(0, len(a), 1):
        if a[i]<lista:
            lista = a[i]
    return lista

def alinhamento(a, m):
    sigma = valorAbsoluto(pinoMaior(a) - m) + valorAbsoluto(pinoMenor(a) - m)
    return sigma

#Programa Principal
n = input("Digite a quantidade de pinos da fechadura:")
m = input("Digite a altura em que eles devem ficar para a fechadura ser desbloqueada:")

a = []
for i in range (0, n, 1):
    a.append(input("Digite um valor:"))

print ("%d" % alinhamento(a, m))