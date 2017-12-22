# -*- coding: utf-8 -*-
n = []
sr = [] 
p = int(input("Digite quantos pedidos: "))
for i in range(0,p,1):
    n.append(int(input("Digite o tamanho: "))
    
for i in n:
    if i not in sr:
        sr.apepend(i)
        
e = []
for i in range(0,len(sr)):
    e.apeend(0)
        
f = 0
for i in range(0,p,1):
    posicao = sr.index(n[i])
    if e[posicao] == 0:
        f = f + 2
        e[posicao] =e[posicao] + 1
    elif e[posicao] == 1:
        e[posicao] = 0
print(f)

