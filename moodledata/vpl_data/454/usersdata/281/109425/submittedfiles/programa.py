# -*- coding: utf-8 -*-
c=int(input('Digite o número de consutas ao estoque: '))

m=[]
for i in range(0,c,1):
    m.append(int(input('Digite o tamanho do %d taco: '% (i+1))))
    
