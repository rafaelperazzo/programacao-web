# -*- coding: utf-8 -*-

nc=int(input('Digite o Número de Competidores:'))
np=int(input('Digite o Número Minimo de Pontos para ser Convidado:'))
pontos=0
cont=0
for i in range (1, nc+1, 1):
    np1=int(input('Digite o Número de Pontos Obtidos na Primeira Fase:'))
    np2=int(input('Digite o Número de Pontos Obtidos na Segunda Fase:'))
    pontos=np1+np2
    if(pontos>=np):
        cont=cont+1
print(cont)