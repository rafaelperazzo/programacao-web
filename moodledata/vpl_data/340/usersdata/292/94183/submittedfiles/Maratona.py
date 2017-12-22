# -*- coding: utf-8 -*-
n = int(input("Digite o número de postos de água durante o trajeto: "))
m = int(input("Digite a distância intermediária máxima de um atleta, em metros: "))
k, cont = [0], 0

k.append(int(input("Digite a posição do 2º posto de água (já sei que o 1º está no ponto de partida), em metros: ")))
if n>2:
    for i in range(3, n+1):
        k.append(int(input("Digite a posição do %d posto de água, em metros: "%i)))
del n

for i in range(0, len(k)-1):
    if (k[i+1] - k[i]) > m:
        cont += 1
del k, m
        
if cont == 0:
    print("S")
    
else:
    print("N")