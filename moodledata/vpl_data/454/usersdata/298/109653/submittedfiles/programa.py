# -*- coding: utf-8 -*-
c=int(input('Digite o numero de consultas: '))

comp=[[],[]]
for i in range (0, c, 1):
    co=0
    co=int(input('Digite o comprimento do taco: '))
    if not co in comp[0]:
        comp[0].append(co)
        comp[1].append(1)
    if co in comp[0]:
        ind=comp[0].index(co)
        comp[1][ind]+=1

print(comp)

