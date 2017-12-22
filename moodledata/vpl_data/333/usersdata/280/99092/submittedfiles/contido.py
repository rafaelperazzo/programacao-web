# -*- coding: utf-8 -*-
n=[]
m=[]
cont=0
quanta=int(input("Digite a quantidade de elementos de a: "))
quantb=int(input("Digite a quantidade de elementos de a: "))
for i in range(0,quanta,1):
    n.append(int(input("Digite um elemento em n: ")))
for i in range(0,quantb,1):
    m.append(int(input("Digite um elemento em n: ")))

for i in range(0,quanta,1):
    for j in range(0,quantb,1):
        if n[i] == m[j]:
            cont = cont + 1

print(cont)