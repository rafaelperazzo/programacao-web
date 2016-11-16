# -*- coding: utf-8 -*-
from __future__ import division

def crescente(a):
    cont=0
    for i in range (1,len(a),1):
        if a[i]<a[i+1] and a[i]>a[i-1]:
            cont=cont+1
    if cont==1:
        return True
    else:
        return False
        
        
a=[]
n=int(input("Digite um valor: "))

for i in range: 
    a.append(input("digite os valoresa da lista: "))

if crescente(a):
    print ("S")
else:
    print ("N")
        


#escreva as demais funções





#escreva o programa principal
