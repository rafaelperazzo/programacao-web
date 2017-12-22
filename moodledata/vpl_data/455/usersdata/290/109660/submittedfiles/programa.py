# -*- coding: utf-8 -*-
n=int(input("Digite a dimensão da matriz: "))
while n<3:
    n=int(input("Digite a dimensão da matriz: "))
matriz=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input("Digite o valor para a matriz: ")))
    matriz.append(linha)
    
sl=[]
for i in range(0,n,1):
    sl.append(sum(matriz[i]))

sc=[]
for j in range(0,n,1):
    c=0
    for i in range(0,n,1):
        c=c+matriz[i][j]
    sc.append(c)
b=[sl[0]]
ct=0
k=0
valorerrado=0
valorcorreto=0
for i in range(0,n,1):
    if sl[i] in b:
        continue
    else:
        ct+=1
        k=i
if ct==1:
    valorerrado=sl[k]
    valorcorreto=sl[0]
if ct!=1:
    valorerrado=sl[0]
    valorcorreto=sl[1]
    k=0

b1=[sc[0]]
ct1=0
k1=0
valorerrado1=0
for i in range(0,n,1):
    if sc[i] in b1:
        continue
    else:
        ct1+=1
        k1=i
if ct1==1:
    valorerrado1=sc[k1]
if ct1!=1:
    valorerrado1=sc[0]
    k1=0

        
        


original=valorcorreto-(valorerrado-matriz[k][k1])
posterior=matriz[k][k1]
print(original)
print(posterior)