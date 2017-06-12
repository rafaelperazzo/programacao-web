# -*- coding: utf-8 -*-
n=int(input('Digite o Número de Competidores:')) 
P=int(input('Digite o Número Minimo de Pontos para ser Convidado:'))
pontos=0    
cont=0
for i in range(1,n+1,1):
    p1=int(input('Digite o Número de Pontos Obtidos na Primeira Fase:'))
    p2=int(input('Digite o Número de Pontos Obtidos na Segunda Fase:'))
    pontos=p1+p2
if pontos>=P:
    cont=cont+1
print(cont) 
