# -*- coding: utf-8 -*

n=int(input("Dimensão do Quadrado: "))
while not n>=3:
    n+int(input("Dimensão do Quadrado: "))

M=[]
for i in range (0,n,1):
    L=[]
    for j in range (0,n,1):
        L.append(int(input("Elemento da Linha: ")))
    M.append(L)

SL=[]
for i in range (0,n,1):
    SL.append(sum(M[i]))

SC=[]
for i in range (0,n,1):
    C=0
    for i in range (0,n,1):
        SC.append(C)

B=[SL[0]]
Cont=0
K=0
CE=0
VC=0
for i in range (0,n,1):
    if SL[i] in B:
        continue
    else:
        Cont=Cont+1
        K=i

if Cont==1:
    VE=SL[K]
    VC=SL[0]

if Cont!=1:
    VE=SL[0]
    VC=SL[1]
    K=0

B1=[SC[0]]
Cont1=0
K1=0
VE1=0

for i in range (0,n,1):
    if SC[i] in B1:
        continue
    else:
        Cont2=Cont2+1
        K1=i

if Cont==1:
    VE1=SC[K1]

if Cont1!=1:
    VE1=SC[0]
    K1=0

O=VC-(VE-M[K][K1])
P=M[K][K1]
print(O)
print(P)