# -*- coding: utf-8 -*-
sala=int(float("digite a quantidade de salas:"))
list=[]
for i in range (0,n,1):
    vida=int(input("digite a quantidade de vidas em cada sala")) 
    list.append(vida)
entrada=int(input("digite a porta de entrada:"))
saida=int(input("digite a porta de saída"))
numero_de_vidas=0
for i in range (entrada,saida+1,1):
    numero_de_vida=numero_de_vida+list[i]

