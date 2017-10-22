# -*- coding: utf-8 -*-
n=int(input("Número de participantes: "))
p=int(input("Pontuação Mínima: "))
cont=0
for i in range (0,n,1):
    f1=int(input("Pontuação na fase 1: "))
    f2=int(input("Pontuação na fase 2: "))
    if f1 + f2 >= p:
        cont = cont + 1
print(cont)