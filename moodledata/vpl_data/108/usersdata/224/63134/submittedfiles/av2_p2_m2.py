# -*- coding: utf-8 -*-
sala=[]
q=int(input('Quantidade de salas: '))
for i in range(0,q,1):
    vidasDeCadaSala=int(input('Digite a quantidade de vidas de cada sala: '))
    sala.append(vidasDeCadaSala)
portaDeEntrada=int(input('Digite a porta de entrada do jogo: '))
portaDeSaida=int(input('Digite a porta de saída do jogo: '))
somatório=0
for i in range(portaDeEntrada,portaDeSaida+1,1):
    somatório=somatório+sala[i]
print(somatório)