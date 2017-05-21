# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('Digite:'))
list=[]
for i in range(1,a+1,1):
    n=int(input('Digite:'))
    list=list+[n]
print(max(list)) 
print(min(list))
print(list.sort())