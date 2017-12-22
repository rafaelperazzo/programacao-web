# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def mosterio(x):
    cont=0
    for i in range (2,x,1):
        if x%i==0:
            cont=cont+1
            break
    if cont==0:
        return true
    else:
        return false
        
y=100
for i in range(1,y,1):
    if misterio(i):
        print(i)

