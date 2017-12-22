# -*- coding: utf-8 -*-
m=int(input('digite o numero de quadras no sentido leste-oeste: '))
n=int(input('digite o numero de quadras no sentido norte-sul: '))
for i in range(0,m,1):
    l=[]
    for j in range(0,n,1):
        l.append(float(input('digite o valor da quadra: ')))
vc1=l[0][0]+l[0][1]