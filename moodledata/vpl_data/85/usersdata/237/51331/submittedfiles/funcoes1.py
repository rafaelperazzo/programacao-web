# -*- coding: utf-8 -*-

def crescente (lista):
    c=0
    p=(len(lista)-1)
    #escreva o código da função crescente aqui
    for i in range (1,len(lista),1):
        if lista[i]>lista[i-1]:
            c=c+1
    if c==p
        return true
    else:
        return false
        
#escreva as demais funções
def decrescente (lista):
    e=0
    o=(len(lista)-1)
    for i in range (1,len(lista),1):
        if lista[i]<lista[i-1]:
            e=e+1
    if e==o
        return true
    else:
        return false
        
def consecultivo (lista):
    for i in range (1,len(lista),1)
        if lista[i]=lista[0]:
            return true
        else:
            return false
        
#escreva o programa principal
n=int(input("Digite n: "))
a=[]
for i in range (0,n,1):
    a.append(int(input("Digite um termo: ")))
    
if crescente (lista):
    print("S")
else:
    print("N")
if decrescente (lista):
    print("S")
else:
    print("N")
if consecultivo (lista):
    print("S")
else:
    print("N")    