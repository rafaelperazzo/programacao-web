# -*- coding: utf-8 -*-
compet=int(input("Digite o numero de competidores: "))
v=int(input("Digite a pontuação para ser aprovado: "))
p=[]
for i in range (0,compet,1):
    a=int(input("Digite a primeira nota do candidato %dº: "%(i+1)))
    b=int(input("Digite a segunda nota do candidato %dº: "%(i+1)))
    p.append(a+b)
cont=0    
for i in range (0,compet,1):
    if p[i]>=v:
        cont+=1
print (cont)
        