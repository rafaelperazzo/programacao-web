# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
i=0
j=p
while j>0:
    j=j//10
    i=i+1
cont=0
while q>0:
    resto=q%(10**i)
    if resto==p:
        cont=cont+1
    q=q//10
if cont!=0:
    print(sim)
else:
    print(Não)

