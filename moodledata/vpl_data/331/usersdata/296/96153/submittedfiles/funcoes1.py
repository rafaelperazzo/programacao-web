# -*- coding: utf-8 -*-
n = int(input("Digite a quantidade de elementos das listas: "))
while n<=1:
    n = int(input("Digite a quantidade de elementos das listas: "))
a = []
for i in range (0,n,1):
    a.append(int(input("Digite um valor para a lista a: ")))
b = []
for i in range (0,n,1):
    b.append(int(input("Digite um valor para a lista b: ")))
c = []
for i in range (0,n,1):
    c.append(int(input("Digite um valor para a lista c: ")))

#escreva o código da função crescente aqui
def crescente (n,l_crescente):
    cont_crescente = 0
    for i in range (0,n-1,1):
        if l_crescente[i]<l_crescente[i+1]:
            cont_crescente = cont_crescente + 1
    if cont_crescente == len(l_crescente) - 1:
        return ("S")
    else:
        return ("N")
    
  

#(0,len(a0 - 1,1)




#escreva as demais funções
def decrescente (n,l_decrescente):
    cont_decrescente = 0
    for i in range (0,n-1,1):
        if l_decrescente[i]>l_decrescente[i+1]:
            cont_decrescente = cont_decrescente + 1
        if cont_decrescente==len(l_decrescente)-1:
            return("S")
        else:
            return("N")
def consecutivos_iguais(n,l_consecutivos):
    cont_consecutivos = 0
    for i in range (0,n-1,1):
        if l_consecutivos[i]==l_consecutivos[i+1]:
            cont_consecutivos = cont_consecutivos + 1
        if cont_consecutivos>0:
            return ("S")
        else:
            return ("N")

#escreva o programa principal
if crescente(a):
    print ("S")
else:
    print("N")
if crescente(b):
    print ("S")
else:
    print("N") 
if crescente(c):
    print ("S")
else:
    print("N")
if decrescente(a):
    print ("S")
else:
    print("N")
if decrescente(b):
    print ("S")
else:
    print("N")
if decrescente(c):
    print ("S")
else:
    print("N")
if consecutivos_iguais(a):
    print ("S")
else:
    print("N")
if consecutivos_iguais(b):
    print ("S")
else:
    print("N")
if consecutivos_iguais(c):
    print ("S")
else:
    print("N")
    
