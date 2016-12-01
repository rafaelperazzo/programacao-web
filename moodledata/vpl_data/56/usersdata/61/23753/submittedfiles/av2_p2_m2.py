# -*- coding: utf-8 -*-
from __future__ import division

def sum(qp,ent,s):
    f=[]
    soma=0
    for i in range(ent, s+1, 1):
        soma=soma+qp[i]
        return soma
        
qp=input("Digite a quantidade de portas: ")
ent=input("Digite a porta de entrada: ")
s=input("Digite a porta de saída: ")
a=[]
for i in range(0,qp,1):
    a.append(int(input("Digte o valor de cada porta: ")))
print ("O número de vidas obtidas é: %d" %sum(a,ent,s))