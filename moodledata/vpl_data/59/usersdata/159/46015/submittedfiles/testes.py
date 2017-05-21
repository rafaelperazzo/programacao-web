# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
x=int(input('Digite nota:'))
maior=x
x=0
for i in range (2,n+1,1):
    nota=int(input('Digite nota:'))
    if nota>=maior:
        maior=nota
    elif nota<x:
        x=nota
    menor=x    
print(menor)
print(maior)
    