# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    c = 0
    for i in range(0,len(lista,1):
        if (i==0):
            if (lista[0]<lista[1]):
                c = c+1
        elif (i==(len(lista)-1)):
            if (lista[len(lista)-2]<lista[len(lista)-1]):
                c = c+1
        else:
            if (lista[i-1] < lista[i]< lista[i+1]):
                c = c+1
    if c==len(lista):
        return (True)
    else:
        return (False)


#escreva as demais funções
def decre (lista):
    c = 0
    for i in range(0,len(lista,1):
        if (i==0):
            if (lista[0]>lista[1]):
                c = c+1
        elif (i==(len(lista)-1)):
            if (lista[len(lista)-2]>lista[len(lista)-1]):
                c = c+1
        else:
            if (lista[i-1] > lista[i] > lista[i+1]):
                c = c+1
                
    if c==len(lista):
        return (True)
    else:
        return (False)

def conig(lista):
c = 0
    for i in range(0,len(lista,1):
        if (i==0):
            if (lista[i]==lista[i+1]:
                c = c+1
        elif (i==(len(lista)-1)):
            if (lista[i-1]==lista[i]:
                c = c+1
        else:
            if (lista[i]==lista[i+1] or (lista[i-1]==lista[i]:
                c = c+1
                
    if (c!= 0) :
        return (True)
    else:
        return (False)


#escreva o programa principal

n = int(input("Digite n: "))

a = []
b = []
c = []

for i in range (0,n1):
    va = float(input("Digite o elemento da primeira lista: "))
    a.append (va)
    
    vb = float(input("Digite o elemento da primeira lista: "))
    b.append (vb)
    
    vc = float(input("Digite o elemento da primeira lista: "))
    c.append (vc)
    
if cres (a):
    print ("S")
else:
    print ("N")
    
if decre (a):
    print ("S")
else:
    print ("N")
    
if conig (a):
    print ("S")
else:
    print ("N")
if cres (b):
    print ("S")
else:
    print ("N")
if decre (b):
    print ("S")
else:
    print ("N")
if conig (b):
    print ("S")
else:
    print ("N")
if cres (c):
    print ("S")
else:
    print ("N")
if decre (c):
    print ("S")
else:
    print ("N")
if conig (c):
    print ("S")
else:
    print ("N")


