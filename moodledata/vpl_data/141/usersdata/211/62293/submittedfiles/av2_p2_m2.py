# -*- coding: utf-8 -*-
K=int(input('escreva a quantidade de portas:'))
C=int(input('escreva a porta de entrada:'))
P=int(input('escreva a porta de saída:'))
H=[]
for i in range(0,q,1):
    V=int(input('escreva a vida:'))
    H.append(V)
Soma=0
for i in range(C,P+1,1):
    Soma=Soma+H[i]
print(Soma)
    



