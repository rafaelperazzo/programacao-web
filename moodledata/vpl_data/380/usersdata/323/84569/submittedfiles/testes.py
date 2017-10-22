# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
cont=0
for i in range(2,n,1):
    if n%i==0:
        cont+=1
if cont>0:
    print('%d n e primo' %n)
else:
    print('%d e primo'%n)