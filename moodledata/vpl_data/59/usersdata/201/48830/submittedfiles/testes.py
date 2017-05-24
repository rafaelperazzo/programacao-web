# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
sm=float(input('Digite um valor:'))
print(sm)
if 0<=sm<=500:
    print('Nunhum crédito')
if 500<sm<=1000:
    i=sm*0.3
    print(i)
if 1000<sm<=3000:
    i=sm*0.4
    print(i)
if sm>300:
    i=sm*0.5
    print(i)