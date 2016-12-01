# -*- coding: utf-8 -*-
from __future__ import division

#Entrada

N = input('Numero de pinos da fechadura: ')
M = input('Altura dos pinos para abrir fechadura: ')


i = 1

lista = [] 

while i <= N :
    lista.append(input('Tamanho do pino: '))
    i = i + 1
    

#Processamento e Saída

j = 0
cont = 0

while j < (N - 1) :
    while lista[j] > M and lista[j + 1] > M :
        lista[j] = lista[j] - 1
        lista[j + 1] = lista[j + 1] - 1
        cont = cont + 1
    
    while lista[j + 1] < M and lista[j] < M :
        lista[j + 1] = lista[j + 1] + 1
        lista[j] = lista[j] + 1
        cont = cont + 1
        
    while lista[j] > M :
        lista[j] = lista[j]- 1
        cont = cont + 1
        
    while lista[j] < M :
        lista[j] = lista[j] + 1
        cont = cont + 1
    j = j + 1
    
    
if  lista[j] != M :
    while lista[j] > M :
        lista[j] = lista[j] - 1
        cont = cont + 1
    while lista[j] < M :
        lista[j] = lista[j] + 1
        cont = cont + 1
        
        

print cont
print lista