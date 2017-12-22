# -*- coding: utf-8 -*-
nl=int(input('Digite o numero de linhas: '))
nc=int(input('Digite o numero de colunas: '))
h=[]
for i in range(0,nl,1):
    c=[]
    for j in range(0,nc,1):
        c.append(int(float(input('digite o valor do elemento'))))
    h.append(c[::-1])
inv=[]
o=len(h)-1
while o>=0:
    inv.append(h[o])
    o-=1
print(inv)
