# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
maior=0
menor=500
for i in range (1,n+1,1):
    idade=int(input('Digite sua idade'))
    if idade>maior:
        maior=idade
    if idade<menor:
        menor=idade
print(maior)
print(menor)