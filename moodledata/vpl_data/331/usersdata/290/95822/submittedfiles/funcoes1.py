# -*- coding: utf-8 -*-
if a==(a.sort()):
    print("S")
    print("N")
if a==(a.sort(reverse=True)):
    print("S")
def crescente(lista):
    #escreva o código da função crescente aqui
    for i in range(0,n,1):
        if a[i]<a[i+1]:
            return True
        else:
            return False

#escreva as demais funções
def decrescente(lista):
    for i in range(0,n,1):
        if a[i]>a[i+1]:
            return True
        else:
            return False
def consecutivos(lista):
    for i in range(0,n,1):
        if a[i]==a[i+1]:
            return True
        else:
            return False





#escreva o programa principal
n=int(input("Digite o valor de n: "))
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(int(input("Digite um valor da lista a: ")))
for i in range(0,n,1):
    b.append(int(input("Digite um valor da lista b: ")))
for i in range(0,n,1):
    c.append(int(input("Digite um valor da lista c: ")))
if crescente(a):
    print("S")
else:
    print("N")
if decrescente(a):
    print("S")
else:
    print("N")
if consecutivos(a):
    print("S")
else:
    print("N")
if crescente(b):
    print("S")
else:
    print("N")
if decrescente(b):
    print("S")
else:
    print("N")
if consecutivos(b):
    print("S")
else:
    print("N")
if crescente(c):
    print("S")
else:
    print("N")
if decrescente(c):
    print("S")
else:
    print("N")
if consecutivos(c):
    print("S")
else:
    print("N")

    
    