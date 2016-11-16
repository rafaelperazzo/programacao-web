# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    #CONTINUE...
    


n = input('Digite a quantidade de elementos da lista: ')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um valor:'))
    
primeiraPosicao=0
for i in range(0,len(a)-1,1):
    if a[i] > a[i+1]:
        primeiraPosicao = i
        break

for i in range(primeiraPosicao,len(a)-1,1):
     if a[i] <= a[i+1]:
         cont=cont + 1
         
if cont ==0 and primeiraPosicao!=0:
    print "S"
else:
    print "N"
         



    
