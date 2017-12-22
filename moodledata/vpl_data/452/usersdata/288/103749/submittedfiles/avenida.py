# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de quadras norte-sul: "))
n=int(input("Digite a quantidade de quadras leste-oeste: "))
while 2<=m<=1000:
    m=int(input("Digite a quantidade de quadras norte-sul: "))
    while 2<=n<=1000:
        n=int(input("Digite a quantidade de quadras leste-oeste: "))
matriz=[]
for i in range (0,m,1):
    while 0<=i<=m-1:
        linha=[]
        for j in range (0,n,1):
            0<=j<=n-1:
            linha.append (int(input("Digite um valor para a quadra: "))) 
            print (matriz[i])