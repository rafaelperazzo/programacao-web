# -*- coding: utf-8 -*-

def crescente (a,n):
    cont=0
    for i in range (n-1):
        if a[i]<a[i+1]:
            cont+=1
    if cont==n:
        print("S")
    else:
        print("N")
        
def decrescente (a,n):
    cont=0
    for i in range (n-1):
        if a[i]>a[i+1]:
            cont+=1
    if cont==n:
        print("S")
    else:
        print("N")
a=[]
b=[]
c=[]
n=int(input("Digite o tamanho da lista:"))

for i in range (n):
    a.append(int(input("Digite um elemento para lista a: ")))
for i in range (n):
    b.append(int(input("Digite um elemento para lista b: ")))
for i in range (n):
    c.append(int(input("Digite um elemento para lista c: ")))
    
    

crescente (a,n)
decrescente (a,n)
crescente (b,n)
decrescente (b,n)
crescente (c,n)
decrescente (c,n)
    
'''def crescente (a,n):
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
        print("N")'''
        
         
        
    
        