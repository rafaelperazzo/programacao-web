# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
for i in range(1000,10000,1):
    a1=i%100
    a2=i//10
    if (a1+a2)*(a1+a2)==i:
        print(i)