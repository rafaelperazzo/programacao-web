# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite a quantidade de alunos:'))
maior=0
menor=500
for i in range(1,n+1,1):
    atual=int(input('digite a nota:'))
    if atual>maior:
        maior=atual
    if atual<menor:
        menor=atual
print(maior)
print(menor)