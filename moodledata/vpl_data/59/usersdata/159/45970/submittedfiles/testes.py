# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
i=1
a=0
while i<=n:
    q=int(input('Digite q:'))
    if q>a:
        dia=i
        quant=q
    a=q
    i=i+1
print(i)
print(quant)
    