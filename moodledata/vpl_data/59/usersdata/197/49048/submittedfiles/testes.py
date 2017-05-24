# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
maior=500
menor=0
for i in range (1,n+1,1):
    idade=int(input('Digite sua idade'))
    if idade>menor:
        menor=idade
    if idade<maior:
        maior=idade
print(maior)
print(menor)