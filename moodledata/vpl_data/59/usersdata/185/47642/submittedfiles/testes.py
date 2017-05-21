# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
h=float(input('digite sua altura:'))
sexo=int(input('digite seu sexo, 1 para masculino e 2 para feminino:'))
peso=float(input('digite seu peso:'))
if sexo==1:
    pesoideal=(72.7*h)-58
else:
    pesoideal=(62.1*h)-44.7
if pesoideal==peso:
    print('esta dentro do peso')
elif pesoideal<peso:
    print('esta abaixo do peso')
else:
    print('esta acima do peso')
