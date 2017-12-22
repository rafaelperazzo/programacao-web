# -*- coding: utf-8 -*-
while True:
    m=int(input('Digite numero de linhas: '))
    if m>=2 and m<=1000:
        break
while True:
    n=int(input('Digite numero de linhas: '))
    if n>=2 and n<=1000:
        break    
    
matriz=[]

for i in range(m):
    linhas=[]
    for j in range(n):
        linhas.append(int(input('Digite os elementos')))
    matriz.append(linha)
    
nt=[]
for i in range(n):
    linhas=[]
    for j in range(m):
        linhas.append(matriz[j][i])))
    nt.append(linhas)
    
soma=1000
for i in range(n):
    if sum(nt[i])<soma:
        soma=sum(nt[i])
print(soma)
