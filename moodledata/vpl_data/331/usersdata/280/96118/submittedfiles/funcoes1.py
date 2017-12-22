# -*- coding: utf-8 -*-

def crescente (lista,n):
    cont = 0
    for i in range (0,n-1,1):
        if lista[i] < lista[i+1]:
            cont = cont + 1
    if cont == n-1:
        return(print("S"))
    else:
        return(print("N"))

def decrescente (lista,n):
    cont = 0
    for i in range (0,n-1,1):
        if lista[i] > lista[i+1]:
            cont = cont + 1
    if cont == n-1:
        return(print("S"))
    else:
        return(print("N"))

def iguais (lista,n):
    cont = 0
    for i in range (0,n-1,1):
        if lista[i] == lista[i+1]:
            cont = cont + 1
    if cont != 0:
        return(print("S"))
    else:
        return(print("N"))


#escreva as demais funções

#escreva o programa principal

a=[]
b=[]
c=[]
n=int(input("Digite n: "))
for i in range (0,n,1):
    a.append(int(input("Digite o termo % da lista a: " %(i+1))))
for i in range (0,n,1):
    b.append(int(input("Digite o termo % da lista b: " %(i+1))))
for i in range (0,n,1):
    c.append(int(input("Digite o termo % da lista c: " %(i+1))))
    
print(crescente(a,n))
print(decrescente(a,n))
print(iguais(a,n))

print(crescente(b,n))
print(decrescente(b,n))
print(iguais(b,n))

print(crescente(c,n))
print(decrescente(c,n))
print(iguais(c,n))






