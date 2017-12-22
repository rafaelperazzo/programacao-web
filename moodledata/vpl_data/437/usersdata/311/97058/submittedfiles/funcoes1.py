# -*- coding: utf-8 -*-
lista=[]
def crescente(lista):
    #escreva o códintgo da função crescente aqui
   for i in range (0,n,1):
        while lista[i]<lista[i+1]:
            return ('S')
        else:
            return ('N')

#escreva as demais funções
def decrescente(lista):
    for i in range(0,n,1):
        while lista[i] > lista[i+1]:
            return True
        else:
            return False
def igualdade(lista):
    for i in range(0,n,1):
        while lista[i]==lista[i+1]:
            return  ('S')
        else:
            return ('N')



n=int(input('Digite o numero abaixo: '))
a=[]
b=[]
c=[]
for i in range (0,n,1):
    a.append(input('Digite o numeroa: '))
for i in range (0,n,1):
    b.append(input('Digite o numerob: '))
for i in range (0,n,1):
    c.append(input('Digite o numeroc: '))
if decrescente(a)== True:
    print ('S')
else:
    print ('N')

    





