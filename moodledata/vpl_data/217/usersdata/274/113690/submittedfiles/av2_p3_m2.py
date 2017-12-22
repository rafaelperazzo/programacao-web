# -*- coding: utf-8 -*

n=int(input("Dimensão do Quadrado: "))
while notn>=3:
    n=int(input("Dimensão do Quadrado: "))
M=[]
for i in range(0,n,1):
    L=[]
    for j in range(o,n,1):
        L.append(int(input("Elemento da Linha: ")))
    M.append(L)
somaL=[]
for i in range(0,n,1):
    somaL.append(sum(M[i]))

somaC=[]
for j in range(0,n,1):
    C=0
    for i in range (0,n,1):
        C=C+M[i][j]
    somaC.append(C)
b=[somaL[0]]
cont=0
k=0
VE=0
VC=0
for i in range(0,n,1):
    if somaL[i] in b:
        continue
    else:
        cont=cont+1
        k=1
if ct==1:
    VE=somaL[k]
    VC+somaL[0]
if ct!=1:
    VE=somaL[0]
    VC+somaL[1]
    k=0

b2=[somaC[0]]
cont2=0
k2=0
VE2=0
for i in range(0,n,1):
     if somaC[i]in b2:
        continue
    else:
        ct2=ct2+1
        k2=i
if cont2==1:
    VE2=somaC[k2]
if ct!=1:
    VE2=somaC[0]
    k2=0

O=VC-(VE-M[k][k2])
P=M[k][k2]
print(O)
print(P)
    
    
    