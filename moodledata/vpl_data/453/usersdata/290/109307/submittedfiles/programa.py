# -*- coding: utf-8 -*-
n=int(input("Digite a dimensão do quadrado: "))
while n<3:
    n=int(input("Digite o valor de n: "))
m=[]
for i in range(0,n,1):
    l=[]
    for j in range(0,n,1):
        l.append(int(input("Digite o seu elemento: ")))
    m.append(l)
a=0
for i in range(0,n-1,1):
    for j in range(0,n,1):
        if sum(m[i])-m[i][j]<sum(m[i+1])-m[i+1][j]:
            a=sum(m[i+1])-m[i+1][j]
        else:
            a=sum(m[i])-m[i][j]
print(a)
        