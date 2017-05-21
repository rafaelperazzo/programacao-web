# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
e=0
fat=1
for i in range (0,n,1):
    fat=fat*i
    x=1/(fat)
    e=e+x
print(e)    
    