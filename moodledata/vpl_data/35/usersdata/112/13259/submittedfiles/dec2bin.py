# -*- coding: utf-8 -*-
from __future__ import division
a=0
n=input('Digite a quanidade de número de:')
j=input('Digite o número:')
l=input('Digite a quanidade números que contém o subnúmero desejado:')
k=input('Digite o subnúmero que desejaachar:')

while a<n:
    a=a+1
    kq=j/(10**l-1)
    if kq==k:
        print('É subnúmero')
    elif kq!=k:
        print ('Não é subnúmero')