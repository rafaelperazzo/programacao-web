# -*- coding: utf-8 -*-
n=int(input('n: '))
a=0
for i in range(0,n,1):
    idade=int(input('digite: '))
    a=a+idade
    
media=a/n
print('%.2f' %media)