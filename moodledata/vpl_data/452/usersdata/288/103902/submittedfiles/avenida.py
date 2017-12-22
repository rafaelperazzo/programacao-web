# -*- coding: utf-8 -*-
matriz=[]
m=0
n=0 
while 2<=m<=1000:
    m=int(input("Digite a quantidade de quadras norte-sul: "))
while 2<=n<=1000:
    n=int(input("Digite a quantidade de quadras leste-oeste: "))
i=0
j=0
if 0<=i<=m-1:
    for i in range (0,m,1):
        linha=[]
        if 0<=j<=n-1:
            for j in range (0,n,1):
               if 0<=j<=n-1:
                    linha.append (int(input("Digite um valor para a quadra: "))) 
        matriz.append(linha)            
    print (matriz)