# -*- coding: utf-8 -*-

def pico(lista):
    pos=0
    i=0
    while (i<=len(lista) and lista[i]<lista[i+1]):
        pos=pos+1
        i=i+1
    if pos==0:
        return False
    else:
        while pos<=len(lista) and lista[pos]>lista[pos+1]:
            pos+=i
    if pos==len(lista):
        return True
    else:
        return False 
        
        

        
    





n=int(input('Digite n: '))
lista=[]
for i in range(0,n,1):
    lista.append(int(input('Digite a quantidade de elementos da lista: ')))
if pico(lista):
    print("'S'")
else:
    print("'N'")

