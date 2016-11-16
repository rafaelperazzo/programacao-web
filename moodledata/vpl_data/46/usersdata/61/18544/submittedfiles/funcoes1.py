# -*- coding: utf-8 -*-
from __future__ import division

def crescente(a):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i]>a[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
        
def decresc(a):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i]>a[i-1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
    
a=[]
b=[]
c=[]
n=int(input("Digite um valor: "))
for i in range(0,n,1):
    a.append(input("Digite um número: "))
if crescente(a):
    print ("S")
else:
    print ("N")

for i in range(0,n,1):
    a.append(input("Digite um número: "))
if decresc(a):
    print ("S")
else:
    print ("N")
    


        


#escreva as demais funções





#escreva o programa principal
