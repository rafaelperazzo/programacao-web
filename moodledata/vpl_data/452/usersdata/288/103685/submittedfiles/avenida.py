# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de quadras norte-sul: "))
n=int(input("Digite a quantidade de quadras leste-oeste: "))
matriz=[]
for i in range (0,m,1):
    linha=[]
    for j in range (0,n,1):
        linha.append (int(input("Digite um valor para a quadra: "))) 