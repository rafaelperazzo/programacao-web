# -*- coding: utf-8 -*-
N=int(input("Digite o número de competidores: "))
P=int(input("Digite o número de pontos mínimos necessários: "))
o=[]
k=0
for i in range (0,N,1):
    o.append(int(input("digite os pontos: )))
for i in range (0,len(o),2):
    if o[i]+o[i+1]==P:
        k=k+1
print(k)
    

