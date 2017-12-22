# -*- coding: utf-8 -*-

def crescente (lista):
    for i in range (0,len (lista),1):
        if lista[i] < lista[i+1]:
            p=('S')
        else:
            p=('N')
            break
    print (p)

def decrescente (lista):
    for i in range (0,len (lista),1):
        if lista[i] > lista[i+1]:
            p=('S')
        else:
            p=('N')
            break
    print (p)
    

def igual (lista):
    for i in range (0,len (lista),1):
        if lista[i] == lista[i+1]:
            p=('S')
            break
        else:
            p=('N')
    print (p)
            



n=int(input())
a = []
b = []
c = []

for i in range (0,n,1):
    a.append(int(input()))

for i in range (0,n,1):
    b.append(int(input()))
    
for i in range (0,n,1):
    c.append(int(input()))

crescente(a)
decrescente(a)
igual(a)

crescente(b)
decrescente(b)
igual(b)

crescente(c)
decrescente(c)
igual(c)
