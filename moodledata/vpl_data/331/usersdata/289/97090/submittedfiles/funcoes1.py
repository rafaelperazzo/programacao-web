# -*- coding: utf-8 -*-

def crescente (lista):
#escreva o código da função crescente aqui
    c=0
    for i in range (0,n,1):
        if i<(n-1):
            if lista[i]<lista[i+1]:
                continue
            else:
                c+=1
                
            break
    return c
            
#escreva as demais funções
def decrescente (lista):
    d=0
    for i in range (0,n,1):
        if i<(n-1):
            if lista[i]>lista[i+1]:
                continue
            else:
                d+=1
                break
    return d

def consecutivo (lista):
    co=0
    for i in range (0,n,1):
        if i<(n-1):
            if lista[i]==lista[i+1]:
                co+=1
                break
            else:
                continue
    return co
    
    
    
#escreva o programa principal
n=int(input("Digite a quantidade de elementos:"))
lista1=[]
lista2=[]
lista3=[]
for i in range (0,n,1):
    lista1.append(int(input("digite número%.d da lista 1: " %(i+1))))
for i in range (0,n,1):
    lista2.append(int(input("digite número%.d da lista 2: " %(i+1))))  
for i in range (0,n,1):
    lista3.append(int(input("digite número%.d da lista 3: " %(i+1))))
x = crescente (lista1)
if x==0:
    print("S")
else:
    print("N")
y = decrescente (lista1)
if y==0:
    print("S")
else:
    print("N")
z = consecutivo (lista1)
if z==0:
    print("S")
else:
    print("N")
    
x = crescente (lista2)
if x==0:
    print("S")
else:
    print("N")
y = decrescente (lista2)
if y==0:
    print("S")
else:
    print("N")
z = consecutivo (lista2)
if z==1:
    print("S")
else:
    print("N")

x = crescente (lista3)
if x==0:
    print("S")
else:
    print("N")
y = decrescente (lista3)
if y==0:
    print("S")
else:
    print("N")
z = consecutivo (lista3)
if z==1:
    print("S")
else:
    print("N")