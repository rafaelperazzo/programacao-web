# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite o numero de pessoas:'))
menor=500
maior=0
for i in range(1,n+1,1):
    nota=float(input('digite a nota:'))
    if nota>maior:
        maior=nota
    if nota<menor:
        menor=nota
print(maior)
print(menor)