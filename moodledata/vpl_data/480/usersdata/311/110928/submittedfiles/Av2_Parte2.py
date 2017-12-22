# -*- coding: utf-8 -*-
a=int(input('Digite o numero: '))

digi=0
while a>=1:
    digi+=1
    a=a//10
while digi==0:
    a=int(input('Digite o numero: '))