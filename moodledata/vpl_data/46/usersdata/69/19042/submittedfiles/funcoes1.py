# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
   cont=0
   for i in range (0,len(lista)-1,1):
       if lista [i]>=lista[i+1]:
           cont=cont+1
    if cont==0:
        return True
    else:
        return False
def decrescente (lista):
   cont=0
   for i in range (0,len(lista)-1,1):
       if lista [i]<=lista[i+1]:
           cont=cont+1
    if cont==0:
        return True
    else:
        return False
def consecutivo (lista):
   cont=0
   for i in range (0,len(lista)-1,1):
       if lista [i]==lista[i+1]:
           cont=cont+1
    if cont==0:
        return False
    else:
        return True
n=input('Digite a quantidade de elementos das lista:')