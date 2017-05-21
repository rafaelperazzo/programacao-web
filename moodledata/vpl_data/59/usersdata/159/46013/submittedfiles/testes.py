# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
a=0
for i in range (1,n+1,1):
    q=int(input('Digite q:'))
    if q>a:
        dia=i
        quant=q
    a=q
print(dia)
print(quant)
    