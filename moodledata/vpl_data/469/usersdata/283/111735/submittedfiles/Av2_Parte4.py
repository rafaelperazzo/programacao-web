# -*- coding: utf-8 -*-
M=int(input('Digite o valor de linhas: '))
N=int(input('Digite o valor de colunas: '))

while M<2 and M>1000:
    print('Numero invalido')
    M=int(input('Digite o valor de linhas: '))
while N<2 and N>1000:
    N=int(input('Digite o valor de colunas: '))

a=[]
at=[]
for i in range(0,M,1):
    l=[]
    for j in range(0,N,1):
        b=int(input('Digite o valor da quadra: '))
        while b<1 and b>100:
            print('Valor invalido')
            b=int(input('Digite o valor da quadra: '))
        l.append(b)
    a.append(l)
for k in range(0,N,1):
    o=[]
    for u in range(0,M,1):
        o.append(a[u][k])
    at.append(o)
c=[]
d=[]
for q in range(0,M,1):
    c.append(sum(a[q]))
for r in range(0,N,1):
    d.append(sum(at[r]))
t=sorted(c)
y=sorted(d)
if t[0]<=y[0]:
    print(t[0])
if y[0]<=t[0]:
    print(y[0])
print(a)
print(at)
            
    