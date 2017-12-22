# -*- coding: utf-8 -*-
c=int(input('Digite o numero de consultas: '))

comp=[]
fabr=0
for i in range (0, c, 1):
    linha=[0,0]
    co=int(input('Digite o comprimento do taco: '))
    if not co in comp:
        linha[0]=co
        linha[1]= linha[1]+1
        comp.append(linha)
    for i in range (0, len(comp), 1):
        if co in comp[i]:
            comp[i][1]=comp[i][1]+1

print(comp)
            

