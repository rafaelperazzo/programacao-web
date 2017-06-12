# -*- coding: utf-8 

np=int(input('Digite o número de Postos de Água:'))
m=int(input('Digite a Distância Intermediária Máxima de um Atleta em Metros:'))
js=m
cont=0
for i in range (1, np+1, 1):
    pa=int(input('Digite a Posição dos Postos de Água ao longo do Trajeto:'))
    js=pa-m
    if(js<m):
        cont=cont+1
if(cont!=np):
    print('N')
else:
    print('S')
