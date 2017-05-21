# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
maior=0
menor=0
for i in range (1,n+1,1):
    nota=int(input('Digite nota:'))
    if nota>=maior:
        maior=nota
    else:
        menor=nota
print(menor)
print(maior)

    