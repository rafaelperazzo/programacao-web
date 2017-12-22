# -*- coding: utf-8 -*-


def crescente(lista):
    #escreva o códintgo da função crescente aqui
   for i in range (0,n,1):
        while lista[i]<lista[i+1]:
            return True
        else:
            return False

#escreva as demais funções
def decrescente(lista):
    for i in range(0,n,1):
        while lista[i] > lista[i+1]:
            return True
        else:
            return False
def igualdade(lista):
    for i in range(0,n,1):
        if lista[i+1]==lista[i+2]:
            return True
        else:
            return False
#codigo
lista=[]
n=int(input("Digite o numero abaixo: "))
a=[]
b=[]
c=[]
for i in range (0,n,1):
    a.append(input("digite o numeroa: "))
for i in range (0,n,1):
    b.append(input("digite o numerob: "))
for i in range (0,n,1):
    c.append(input("digite o numeroc: "))
if crescente(a)==True:
    print('S')
else:
    print ('N')
if decrescente(a)== True:
    print ('S')
else:
    print ('N')
if igualdade(a)== True:
    print ('S')
else:
    print ('N')
if crescente(b)== True:
    print ('S')
else:
    print ('N')
if decrescente(b)== True:
    print ('S')
else:
    print ('N')
if igualdade(b)== True:
    print ('S')
else:
    print ('N')
if crescente(c)== True:
    print ('S')
else:
    print ('N')
if decrescente(c)== True:
    print ('S')
else:
    print ('N')
if igualdade(c)== True:
    print ('S')
else:
    print ('N')





