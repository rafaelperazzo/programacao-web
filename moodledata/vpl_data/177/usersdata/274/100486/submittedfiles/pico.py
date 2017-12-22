# -*- coding: utf-8 -*-

def cres(lista):
    if len (lista)==1:
        return (False)
    c = 0
    for i in range (0,len(lista),1):
        if(i==0):
            if((lista[i])<(lista[i+1])):
                c=c+1
        elif(i==(len(lista)-1)):
            if lista[len(lista)-2]<lista[len(lista)-1]:
                c=c+1
        else:
            if((lista[i])<(lista[i+1])):
                c=c+1
    if c==len (lista):
        return (True)
    else:
        return(False)

def decre(lista):
    c = 0
    if len (lista)==1:
        return (False)
    c = 0
    for i in range (0,len(lista),1):
        if(i==0):
            if((lista[i])>(lista[i+1])):
                c=c+1
        elif i == len(lista)-1 :
            if lista[len(lista)-2]>lista[len(lista)-1]:
                c=c+1
        else:
            if((lista[i])>(lista[i+1])):
                c=c+1
    if c==len (lista):
        return (True)
    else:
        return(False)
        
def pico(lista):
    em = max(lista)
    im = lista.index(em)
    a = []
    d = []
    for i in range (0,im+1,1):
        ea = lista[i]
        
        a.append (ea)
        
    for i in range (im+1,len(lista),1):
        ed = lista[i]
        
        d.append (ed)
    if cres (a) and decre (d):
        return(True)
    else:
        returne (False)

n = int(input("Digite a quantidade de elementos da lista: ")):
a = []

for i in range (0,n,1):
    va = float(input("Digite o elemento da lista: "))
    a.append (va)
if pico (a):
    print ("S")
else:
    print ("N")
