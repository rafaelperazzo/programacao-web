# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
e=1
fat=1
for i in range (1,n,1):
    x=1/(fat)
    e=e+x
    fat=fat*i
print(e)    
    