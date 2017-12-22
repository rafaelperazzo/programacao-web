# -*- coding: utf-8 -*-
a=[]
b=[]
c=[]
n=int(input("Digite o tamanho da lista:"))
mt=[]
for j in range (3):
    lista=[]
    for i in range (n):
        lista.append(int(input("Digite um elemento para lista: "))
    mt.append(lista)
    
a=mt[0]
b=mt[1]
c=mt[2]
crescente (a,n)
decrescente (a,n)
crescente (b,n)
decrescente (b,n)
crescente (c,n)
decrescente (c,n)
    
def crescente (a,n):
    cont=0
    for i in range (n):
        if a[i]<a[i+1]:
            cont+=1
    if cont==n:
        print("S")
    else:
        print("N")
        
def decrescente (a,n):
    cont=0
    for i in range (n):
        if a[i]>a[i+1]:
            cont+=1
    if cont==n:
        print("S")
    else:
        print("N")
        
         
        
    
        