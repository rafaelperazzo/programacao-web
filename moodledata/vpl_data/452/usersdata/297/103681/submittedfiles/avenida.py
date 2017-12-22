# -*- coding: utf-8 -*-
m=int(input('digite o número de quadras no sentido norte-sul: '))
n=int(input('digite o número de quadras no sentido leste-oeste: '))
matriz=[]
if 2<=m and m<=1000:
    if 2<=n and n<=1000:
        for i in range(0,m,1):
            linha=[]
            for j in range(0,n,1):
                r=(int(input('digite o valor em milhões que a quadra possui: ')))
                while r<1 or r>100:
                    r=(int(input('digite o valor em milhões que a quadra possui: ')))
                linha.append(r)
            matriz.append(linha)
        barato=0
        for i in range (0,m,1):
            
    else :
        while 2>m or m>1000:
            n=int(input('digite o número de quadras no sentido leste-oeste: '))
else :
    while 2>n or n>1000:
        m=int(input('digite o número de quadras no sentido norte-sul: '))