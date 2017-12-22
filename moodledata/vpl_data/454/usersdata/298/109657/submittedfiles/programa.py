# -*- coding: utf-8 -*-
c=int(input('Digite o numero de consultas: '))

comp=[]
for i in range (0, c, 1):
    comp.append(int(input('Digite o comprimento do taco: ')))

b=[]
for i in range (0, c, 1):
    if not comp[i] in b:
        b.append(comp[i])

v=[]
for i in range (0, len(b), 1):
    v.append(0)

for i in range (0, len(b), 1):
    for j in range (0, c, 1):
        if b[i]==comp[j]:
            v[i]+=1

soma=0
for i in range (0, len(v), 1):
    if (v[i]%2)==0:
        soma+=v[i]
    if (v[i]%2)==1:
        soma+=(v[i]+1)