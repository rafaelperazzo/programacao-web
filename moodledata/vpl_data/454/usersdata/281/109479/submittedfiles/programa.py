# -*- coding: utf-8 -*-
c=int(input('Digite o número de consutas ao estoque: '))
cont=0
l=[]
for i in range(0,c,1):
    l.append(int(input('Digite o tamanho do  taco: ' )))
    if l[i] == l[i+1]:
        cont=cont+0 
    else:
        cont=cont+2
print(cont)
        