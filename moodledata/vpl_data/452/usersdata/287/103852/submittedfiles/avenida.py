# -*- coding: utf-8 -*-
while not n>=2 and n<=1000:
    n=int(input('N: '))
m=int(input('M: '))
matriz=[]
for i in range(0,n,1):
    linhas=[]
    for j in range(0,m,1):
        linhas.append(int(input("qual o valor da quadra %d,%d?" %(n+1,m+1))))
    matriz.append(linhas)
print(matriz)


    

