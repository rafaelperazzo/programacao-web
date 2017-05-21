# -*- coding: utf-8 -*-

n=int(input('Digite n: '))
i=0
cont=0
for i in range(1,n+1,1):
    if i%2==0:
        cont=cont+1
        print(i)