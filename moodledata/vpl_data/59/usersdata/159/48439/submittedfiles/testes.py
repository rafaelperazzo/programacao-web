# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
i=n
cont=0
while i>0:
    x=i%2
    cont=cont+x
    i=i//2
    cont=cont*10
print(cont)    
     
        