# -*- coding: utf-8 -*-
n=input('Digite o número de elementos da primeira lista:')
l1=[]
for i in range(0,n,1):
    l1.append(float(input('digite o valor%d:' %(i+1))))

n=input('Digite o número de elementos da segunda lista:')
l2=[]
for i in range(0,n,1):
    l2.append(float(input('digite o valor%d:' %(i+1))))

lf=[x for x in l1 if x not in l1]
cont=0
while cont<=lf:
    cont=cont+1
print(lf)
print(cont)
