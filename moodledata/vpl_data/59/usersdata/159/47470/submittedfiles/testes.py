# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
cont=0
for i in range (0,n,1):
    cont=((-1)**i)/(2*i+1)
pi=4*cont
print(pi)