# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
while True:
    a=int(input('digite a:'))
    if a>0:
        break
    soma=0
    while a>=1:
        i=a//10
        r=a%10
        soma=soma+r
        a=a//10
        
    print (soma)
        