# -*- coding: utf-8 -*-
n=int(input('tamanho da lista: '))
l=[]
soma=0
for i in range (1,n+1,1):
    l.append(input('elemento da lista: '))
for i in range (0,n-1,1):
    soma=soma + l[i]
media=soma/n
print ('%.2f' %l[0])
print ('%.2f' %l[n-1])
print ('%.2f' %media)
print ('%.2f' %l)