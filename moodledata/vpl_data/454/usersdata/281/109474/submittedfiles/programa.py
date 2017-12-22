# -*- coding: utf-8 -*-
c=int(input('Digite o número de consutas ao estoque: '))
cont=0
m=[]
for i in range(0,c,1):
    m.append(int(input('Digite o tamanho do %d taco: '% (i+1))))
    if m[i] == m[i+1]:
        cont=0 
    else:
        cont=2
print(cont)
        