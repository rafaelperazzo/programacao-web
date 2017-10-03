# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
h = float(input('Digite sua altura: '))
sexo = bool(input('Voce eh homem? (sim:true, nao:false)'))
peso = float(input('Qual seu peso? '))
PH = (72.7*h)-58
PM = (32.1*h)-44.7
if sexo=='sim' and peso>PH:
    print('Voce esta acima do peso')
else sexo=='sim'and peso<=PH:
    print('Seu peso esta normal')
    if sexo=='nao' and peso>PM:
        print('Voce esta acima do peso')
    else sexo=='nao' and peso<=PM:
        print('Seu peso esta normal')
    
