# -*- coding: utf-8 -*-
n=int(input("Digite a dimensão do quadrado: "))
while n<3:
    n=int(input("Digite a dimensão do quadrado: "))
m=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input("Digite o seu elemento: ")))
    m.append(linha)

k=[]
for i in range(0,n,1):
    k.append(sum(m[i]))

d=[]
for j in range(0,n,1):
    c=0
    for i in range(0,n,1):
        c+=m[i][j]
    d.append(c)

l=0
for i in range(0,n,1):
    for j in range(0,n,1):
        if k[i]+d[j]-2*m[i][j]>l:
            l=k[i]+d[j]-2*m[i][j]
print(l)

        