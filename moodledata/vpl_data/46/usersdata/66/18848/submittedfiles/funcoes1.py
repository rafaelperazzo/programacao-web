# -*- coding: utf-8 -*-
from __future__ import division

#[1, 2 ,3 ,4, 5] o último não tem próximo. Então vamos até o penultimo elemento. 
#1) Procurar um elemento que é maior do que o próximo. Se houver algum, não é crescente. 
#2) Verificar se cada elementos é menor do que o próximo. Se a contagem for igual a quantidade de elementos menos
#1, então é crescente. 

def crescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont = cont + 1
    
    if cont!=0:
        return False
    else:
        return True
    

        
def decrescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont = cont + 1
    
    if cont!=0:
        return False
    else:
        return True


#programa principal
n=int(input("digite a quantidade de termos:"))
a=[]
b=[]
c=[]

for i in range (0,n,1):
    a. append(input("Digite os valores da lista a:"))
for i in range (0,n,1):
    b.append(input("Digite os valores da lista b:"))
for i in range (0,n,1):
    c.append(input("digite os valores da lista c:"))
if crescente(a):
    print ("S")
else:
    print ("N")
    
if descrecente(a):
    print ("S")
else:    
    print ("N")
if consecutivos(a):
    print ("S")
else:
    print ("N")
    
if crescente (b):
    print ("S")
else:
    print ("N")
    
if decrescente(b):
   print("S")
else:
   print("N")
if consecutivos(b):
    print("S")
else:
    print("N")


if crescente (c):
    print ("S")
else:
    print ("N")
    
if decrescente(c):
   print("S")
else:
   print("N")
if consecutivos(c):
    print("S")
else:
    print("N")
    





