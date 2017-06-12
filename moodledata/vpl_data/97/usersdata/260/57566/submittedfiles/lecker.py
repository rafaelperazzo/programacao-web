# -*- coding: utf-8 -*-
def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=cont+1
    return cont
a=[]
n=int(input("digite a quantidade de elementos "))
for i in range(0,n,1):
    a.append(int(input("digite o valor do elemento ")))
b=[]
n=int(input("digite a quantidade de elementos "))
for i in range(0,n,1):
    lista2.append(int(input("digite o valor do elemento ")))
if lecker(a)==1:
    print("S")
else:
    print("N")
if lecker(b)==1:
    print("S")
else:
    print("N")