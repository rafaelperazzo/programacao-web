# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
n=input('digite a quantidade de elementos:')
a=[]




#SAIDA
for i in range (0,n,1):
    a.append(input('digite os valores:'))
soma=0
for i in range (0,n,1):
    soma=soma+a[i]
    
    media=soma/n
print ('%.2f' %a[0])
print ('%.2f' %a[n-1])
print ('%.2f' %media)
print (a)
