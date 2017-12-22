# -*- coding: utf-8 -*-
def crescente(x,lista1):
    #escreva o código da função crescente aqui
    a=0
    for i in range(0,x-1,1):
        if lista1[i]<lista1[i+1]:
            a=a+1
    if a==len(lista1)-1:
        return ("S")
    else:
        return ("N")

#escreva as demais funções
def decrescente(x,lista2):
    a1=0
    for i in range(0,x-1,1):
        if lista2[i]>lista2[i+1]:
            a1=a1+1
    if a1==len(lista2)-1:
        return ("S")
    else:
        return ("N")

def consecutivo(x,lista3):
    a2=0
    for i in range(0,x-1,1):
        if lista3[i]==lista3[i+1]:
            a2=a2+1
    if a2>0:
        return ("S")
    else:
        return ("N")
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
print(crescente(n,a))
print(decrescente(n,a))
print(consecutivo(n,a))
print(crescente(n,b))
print(decrescente(n,b))
print(consecutivo(n,b))
print(crescente(n,c))
print(decrescente(n,c))
print(consecutivo(n,c))