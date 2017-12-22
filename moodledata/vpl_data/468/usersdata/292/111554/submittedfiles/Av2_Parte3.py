# -*- coding: utf-8 -*-
########################################### -> MÓDULOS
from math import sqrt

########################################### -> FUNÇÕES
def media(lista):
    MEDIA = sum(lista)/len(lista)
    lista.append(MEDIA)
    
    return MEDIA
    
def dp(lista, MEDIA):
    somat = 0
    
    for i in lista:
        somat += (i-MEDIA)**2
        
    DP = sqrt(somat/(len(lista)-1))
    
    return DP

########################################### -> PROGRAMA PRINCIPAL

m = int(input())
n = int(input())
listas = []
for i in range(m):
    lista = []
    for j in range(n):
        lista.append(int(input()))
        
    listas.append(lista)
    
for i in listas:
    print("%.2f"%media(i))
    print("%.2f"%dp(i, media(i)))