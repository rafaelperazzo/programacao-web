# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite o numero de alunos:'))
menor=10
maior=0
for i in range (1,n+1,1):
    nota=int(input('digite a nota:'))
    if nota>maior:
        maior=nota
    if nota<menor:
        menor=nota
print(maior)
print(menor)