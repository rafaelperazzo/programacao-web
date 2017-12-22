# -*- coding: utf-8 -*-

def lecker(a):
    cont=0
    if a[0]>a[1]:
        cont+=1
    if a[len(lista)-1]>a[len(lista)-2]:
        cont+=1
    for i in range(1,len(lista)-1 ,1):
        if a[i+1]<a[i] and a[i]>a[i-1]:
            cont+=1
    if cont==1:
        return True
    else:
        return False
 
tamanho1=int(input('Digite o tamanho da primeira lista: '))
tamanho2=int(input('Digite o tamanho da segunda lista: '))
lista1=[]
lista2=[]
for i in range(tamanho1):
    lista1.append(int(input('Digite os elementos da primeira lista: ')))
for i in range(tamanho2):
    lista2.append(int(input('Digite os elementos da segunda lista: ')))    


if lecker(lista1):
    print("'S'")
else:
    print("'N'")

if lecker(lista2):
    print("'S'")
else:
    print("'N'")    
    