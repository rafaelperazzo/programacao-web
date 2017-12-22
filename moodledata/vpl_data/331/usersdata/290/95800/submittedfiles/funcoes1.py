# -*- coding: utf-8 -*-
n=int(input("Digite o valor de n: "))
lista=[]
for i in range(0,n,1):
    lista.append(int(input("Digite um valor da lista: ")))
a=0
j=0
m=0
x=0
def crescente (lista):
    for i in lista:
        if lista[i]<lista[i+1]:
            j=j+1
        if lista[i]>lista[i+1]:
            m=m+1
        else:
            x=x+1
    if j==n-1:
        print("S")
    if j!=n-1:
        print("N")
    if m==n-1:
        print("S")
    if m!=n-1:
        print("N")
    if x==0:
        print("S")
    if x!=0
        print("N")
    #escreva o código da função crescente aqui


#escreva as demais funções





#escreva o programa principal
