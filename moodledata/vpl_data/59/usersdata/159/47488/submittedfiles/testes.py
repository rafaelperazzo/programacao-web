# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
e=1
fat=1
i=1
while (1/fat)>0.000001:
    x=1/(fat)
    e=e+x
    fat=fat*i
    i=i+1
print(e)    
    