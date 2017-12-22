# -*- coding: utf-8 -*-
n=int(input("Digite a dimensão do quadrado: "))
m=[]
for i in range(0,n,1):
    l=[]
    for j in range(0,n,1):
        l.append(int(input("Digite o seu elemento: ")))
    m.append(l)
