# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
sm=float(input('Digite um valor:'))
print(sm)
if 0<=sm<=500:
    print('Nunhum crédito')
if 500<sm<=1000:
    i=sm*0.3
    print(i)
    print('30% do saldo médio')
if 1000<sm<=3000:
    i=sm*0.4
    print(i)
    print('40% do saldo médio')
if sm>3000:
    i=sm*0.5
    print(i)
    print('50% do saldo médio')