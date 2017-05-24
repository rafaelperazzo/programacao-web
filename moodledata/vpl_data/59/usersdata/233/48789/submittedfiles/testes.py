# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite um número: '))
nota0=0
maior=0
menor=100000
for i in range(1,n+1,1):
    nota=int(input('Digite um número: '))
    if nota>maior:
        maior=nota   
    if nota<=menor:
        menor=nota
print(maior)
print(menor)
























