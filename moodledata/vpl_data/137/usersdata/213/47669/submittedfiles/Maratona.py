# -*- coding: utf-8 -*-
numeroDePostos=float(input('Informe o número do postos: '))
dmi=float(input('Informe a Distância Média Intermediária: '))

for i in range (1,numeroDePostos,1):
    posicaoDoPosto=float(input('Informe a posição do Posto:'))
    x=posicaoDoPosto
    y=posicaoDoPosto
    if dmi>=posicaoDoPosto:
        print('S')
    else:
        print('N')
    
    