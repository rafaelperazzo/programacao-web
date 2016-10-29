# -*- coding: utf-8 -*-
from __future__ import division
a=0
n=input('Digite a quanidade de números:')
j=input('Digite o número:')
l=input('Digite a quanidade de números que contém o subnúmero desejado:')
k=input('Digite o subnúmero que deseja achar:')

while a<n:
    a=a+1
    kq=j/(10**l-1)-j%(10**l-1)
    if kq==k:
        print('É subnúmero')
    elif kq!=k:
        print ('Não é subnúmero')