# -*- coding: utf-8 -*-
numeroDePostos=int(input('Informe o número do postos: '))
dmi=float(input('Informe a Distância Média Intermediária: '))
y=0
for i in range (1,numeroDePostos+1,1):
    posicaoDoPosto=float(input('Informe a posição do Posto:'))
    x=posicaoDoPosto
    distancia=abs(x-y)
    if dmi>=distancia:
        print('S')
    else:
        print('N')
    y=posicaoDoPosto
    