# -*- coding: utf-8 -*-

def crescente ():
    #escreva o código da função crescente aqui
    c=0
    for i in range (0,n,1):
        if a[i]<a[i+1]:
            continue
        else:
            c+=1
            break
    return c

#escreva as demais funções





#escreva o programa principal
n = int(input("Digite a quantidade de elementos: "))
lista1 = []
lista2 = []
lista3 = []
for i in range (0,n,1):
    lista1.append(float(input("Digite número %.1f da lista 1: " %(i+1))))
    lista2.append(float(input("Digite número %.1f da lista 2: " %(i+1))))
    lista3.append(float(input("Digite número %.1f da lista 3: " %(i+1))))
import funcoes1.py
x = crescente (lista1)
y = crescente (lista2)
z = crescente (lista3)
if x==0:
    print("S")
else:
    print("N")
if y==0:
    print("S")
else:
    print("N")
if z==0:
    print("S")
else:
    print("N")