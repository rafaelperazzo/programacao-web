# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=[2,1,1]
n=int(input('Digite seu numero: '))
i=0
for i in range(0,n-1,1):
    if a[i]<a[i+1]:
        i=+1
if (i==(n-1)):
    print ('S')

