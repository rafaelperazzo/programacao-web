# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
i=1
contador=0
while i<=n:
    if i%2==0:
        contador=contador+i
    i=i+1    
print(contador)        