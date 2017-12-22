# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n=int(input("Digite uma quantidade de elementos:"))

elem = []
dmh=0
mh=0
mg=0


for i in range (0,n,1):
    elem.append(float(input("Digite o elemento %d :" %(i+1))))
    dmh+= 1/float(elem[i])
    
mh = n/dmh
print (mh)

