# -*- coding: utf-8 -*-
from __future__ import division


n=int(input('Digite n:'))

i=0
cont=0
soma=0
cont2=0
soma2=0

while i<n:
    if i%2==1:
        cont+cont+1
    i=i+1
print(cont)


while i>n:
    if i%2==0:
        soma=soma+i
    i=i+1
print(soma)


while i<n:
    if i%2==1:
        cont2=cont2+1
    i=i+1
print(cont2)

while i>n:
    if i%2===0:
        soma2=soma2+1
    i=i+1
print(soma)

