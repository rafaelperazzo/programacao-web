# -*- coding: utf-8 -*-
n=int(input("Digite a dimensão do quadrado: "))
while n<3:
    n=int(input("Digite a dimensão do quadrado: "))
m=[]
print(n)
for i in range(0,n,1):
    l=[]
    for j in range(0,n,1):
        l.append(int(input("Digite o seu elemento: ")))
    m.append(l)
a=0
for i in range(0,n-1,1):
    g=0
    for j in range(0,n,1):
        if sum(m[i])-m[i][j]<sum(m[i+1])-m[i+1][j]:
            a=sum(m[i+1])-m[i+1][j]
            g=i+1
        else:
            a=sum(m[i])-m[i][j]
            g=i
for j in range(0,n,1):
    d=[]
    c=0
    for i in range(0,n,1):
        c=c+m[i][j]
    d.append(c)

for j in range(0,n-1,1):
    e=0
    f=0
    for i in range(0,n,1):
        if d[j]-m[i][j]<d[j+1]-m[i][j+1]:
            e=d[j+1]-m[i][j+1]
            f=j+1
        else:
            e=d[j]-m[i][j]
            f=j
print(g)
print(f)
            
pp=int(input("Digite o valor: ))
        