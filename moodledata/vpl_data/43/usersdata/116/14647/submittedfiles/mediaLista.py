# -*- coding: utf-8 -*-
from __future__ import division

n = input ('insira o valor de n:')

a=[]

for i in range (0,n,1):
    a.append(input('insira um valor:'))
    
cont=0

for j in range (0,n,1):
    cont=cont+a[j]
     
media=cont/n

print ('%.2f' %a[0])
print ('%.2f' %a[n-1])
print ('%.2f' %media)
print (a)
