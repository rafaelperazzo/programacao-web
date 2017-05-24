# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
sm=float(input('Digite um valor:'))
print('Saldo médio:' '%.2f' %sm)
if 0<=sm<=500:
    print('Nunhum crédito')
if 500<sm<=1000:
    i=sm*0.3
    print('Valor do crédito:' '%.2f' %i)
if 1000<sm<=3000:
    i=sm*0.4
    print('Valor do crédito:' '%.2f' %i)
if sm>3000:
    i=sm*0.5
    print('Valor do crédito:' '%.2f' %i)