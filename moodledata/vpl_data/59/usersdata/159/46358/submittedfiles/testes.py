# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
x=int(input('Digite x:'))
k=1
exp=0
cont=0
a=(x**k)/k
while a>=0.001:
    cont=cont+((-1**exp)*a)
    exp=exp+1
    k=k+2
print(cont)    
    

 

    