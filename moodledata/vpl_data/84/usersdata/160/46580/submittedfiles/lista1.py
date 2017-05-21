# -*- coding: utf-8 -*-
from __future__ import division


n=int(input('Digite n:'))

i=0
cont=0
soma=0
cont2=0
soma2=0

for i in range(0,n,1):
    lista=int(input('Digite a lista de números:'))
    while i<lista:
        if i%2==1:
            cont=cont+1
            
        i=i+1
    


    while i>lista:
         if i%2==0:
             soma=soma+i
         i=i+1



    while i<lista:
        if i%2==1:
            cont2=cont2+1
        i=i+1
    

    while i>lista:
        if i%2==0:
             soma2=soma2+1
        i=i+1
    

print(cont)
print(soma)
print(cont2)
print(soma2)
