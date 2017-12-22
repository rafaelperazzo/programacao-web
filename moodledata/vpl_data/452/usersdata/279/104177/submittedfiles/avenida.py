# -*- coding: utf-8 -*-

m=(int(input()))
n=(int(input()))
quadras=[]
soma=0
soma1=0
linhas=[]
colunas=[]
preco=0
preco1=0
for i in range(0,m,1) :
    ruas=[]
    for j in range(0,n,1):
        ruas.append(int(input()))
    quadras.append(ruas)    
for i in range (0,m,1) :
    if i>0 :
     linhas.append(soma)
    for j in range(0,n,1) :
        soma=soma+quadras[i][j]
        
for j in range (0,n,1) :
    if j>0 :
      colunas.append(soma1)
    for i in range (0,m,1) :
        soma1=soma1+quadras[i][j]
    

for i in range(0,m-2,1):
    if linhas[i]<=linhas[i+1] :
        preco=linhas[i]
    else:
        preco=linhas[i+1]

for j in range(0,n-2,1) :
    if colunas[i]<=colunas[i+1] :
        preco1=colunas[i]
    else:
        preco1=colunas[i+1]
if preco1<=preco :
    print(preco1)
else:
    print(preco)
print(linhas)
print(colunas)



