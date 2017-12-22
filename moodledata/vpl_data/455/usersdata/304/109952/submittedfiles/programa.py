# -*- coding: utf-8 -*-

n = int(input('Digite n: '))
while not n>=3:
    n = int(input('Digite n: '))
matriz = []
for i in range (0,n,1):
    linha = []
    for j in range (0,n,1):
        linha.append(int(input('Digite n: ')))
    matriz.append(linha)
somal=[]
for i in range (0,n,1):
    somal.append(sum(matriz[i]))
somac=[]
for j in range (0,n,1):
    c = 0
    for i in range (0,n,1):
        c=c+matriz[i][j]
    somac.append(c)
b=[somal[0]]
ct = 0
k = 0
ve = 0
vc = 0
for i in range (0,n,1):
    if somal[i] in b:
        continue
    else: 
        ct+=1
        k=i
if ct == 1:
    ve=somal[k]
    vc=somal[0]
if ct != 1:
    ve=somal[0]
    vc=somal[1]
    k=0
bl = [somac[0]]
cont2 = 0
kl=0
vel=0
for i in range (0,n,1):
    if somac[i] in bl:
        continue
    else:
        cont2 += 1
        kl = i
if cont2 ==1:
    vel = somac[kl]
if cont2 !=1:
    vel = somac[0]
    kl = 0
o = vc - (ve-matriz[k][kl])
po = matriz[k][kl]
print(o)
print(po)