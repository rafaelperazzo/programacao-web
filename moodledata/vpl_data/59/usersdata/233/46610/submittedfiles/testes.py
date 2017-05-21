# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('n: '))
list=[]
for i in range(1,n+1,1):
    a=int(input('n: '))
    list=list+[a]
list.sort(reverse=True)
print(list)    
