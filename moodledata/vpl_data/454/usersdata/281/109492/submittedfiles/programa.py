# -*- coding: utf-8 -*-
c=int(input('Digite o número de consutas ao estoque: '))

l= []
for i in range(0,c,1):
    l.append(int(input('Digite o tamanho do  taco: ' )))

for i in range (1,8,1):
    print(l[i])
    
        