# -*- coding: utf-8 -*-

L=[]
n=int(input('digite n:'))
soma=0
for i in range (0,n,1):
    m=int(input('digite o numero:'))
    L.append(m)
for i in range(0,len(L),1):
    soma=soma+L[i]
media=soma/len(L)
print('%.2f' %L[0])
print('%.2f' %media)
print('%.2f' %L)