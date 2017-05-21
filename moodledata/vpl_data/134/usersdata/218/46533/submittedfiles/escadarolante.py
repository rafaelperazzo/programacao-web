# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de pessoas:'))
ultima=0
for i in range(0,n,1):
    tempo=int(input('digite o horario:'))
    if tempo>ultima:
        ultima=tempo
print(ultima+10)        