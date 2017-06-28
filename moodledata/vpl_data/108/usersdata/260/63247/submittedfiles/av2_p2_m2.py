# -*- coding: utf-8 -*-
sala=int(input("digite a quantidade de salas:"))
list=[]
for i in range (0,sala,1):
    vida=int(input("digite a quantidade de vidas em cada sala")) 
    list.append(vida)
entrada=int(input("digite a porta de entrada:"))
saida=int(input("digite a porta de saída"))
n=0
for i in range(entrada,saida+1,1):
    n=n+list[i]
print(n)

