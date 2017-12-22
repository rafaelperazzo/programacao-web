# -*- coding: utf-8 -*-

def pico(lista):
    pos=0
    i=0
    while (i<len(lista)-1 and lista[i]<lista[i+1]):
        pos=pos+1
        i=i+1
    if pos==0:
        return False
    else:
        while pos<len(lista)-1 and lista[pos]>lista[pos+1]:
            pos+=1
    if pos==len(lista)-1:
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

