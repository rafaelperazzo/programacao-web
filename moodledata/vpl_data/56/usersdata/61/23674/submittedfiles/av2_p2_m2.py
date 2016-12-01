# -*- coding: utf-8 -*-
from __future__ import division

def sum(quantp,ent,s):
    f=[]
    soma=0
    for i in range(ent, s+1, 1):
        soma=soma+f[i]
        f.append(soma)
        return f
        
        
quantp=input("Digite a quantidade de portas: ")
ent=input("Digite a porta de entrada: ")
s=input("Digite a porta de saída: ")
for i in range(0,len(f),1):
    f.append(int(input("Digte o valor de cada porta: ")))
c=sum(quantp,ent,s)
t=maior(f)
print t