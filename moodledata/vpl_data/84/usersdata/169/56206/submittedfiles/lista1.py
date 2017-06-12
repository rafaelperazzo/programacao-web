# -*- coding: utf-8 -*-
n=int(input('Digite a Quantidade de Elementos da Lista:'))
l1=[]
qpares=0
qimpares=0
spares=0
simpares=0
for i in range(1,n+1,1):
    v=int(input('Digite um Valor para a Lista:'))
    l1.append(v)
for j in range(0,len(l1),1):
    if (l1[k]%2==0):
        qpares=qpares+1
        spares=spares+l1[j]
    else: 
        qimpares=qimpares+1
        simpares=simpares+l1[j]
print(simpares)
print(spares)
print(qpares)
print(qimpares)
print(l1)


