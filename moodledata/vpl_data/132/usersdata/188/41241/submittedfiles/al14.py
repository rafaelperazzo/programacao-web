# -*- coding: utf-8 -*-
n=int(input('Digite o número de pessoas:'))
i=0
termo=n
while termo>0:
    id=int(input('Digite a Idade:'))
    i=i+id
    termo=termo-1
media=(i/n)
print('%.2f'%media)