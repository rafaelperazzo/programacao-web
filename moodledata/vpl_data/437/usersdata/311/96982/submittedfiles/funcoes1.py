# -*- coding: utf-8 -*-
lista=[]
def crescente(lista):
    #escreva o códintgo da função crescente aqui
   for i in range (0,n,1):
        if lista[i]<lista[i+1]:
            return 'S'
        else:
            return 'N'

#escreva as demais funções
def decrescente(lista):
    for i in range(0,n,1):
        while lista[i] > lista[i+1]:
            return 'S'
        else:
            return 'N'
def igualdade(lista):
    for i in range(0,n,1):
        if lista[i]==lista[i+1]:
            return  'S'
        else:
            return 'N'


#escreva o programa principal
a=[]
b=[]
c=[]
n= (int(input('digite a quantidade: ')))
for i in range(0,n,1):
    a.append(int(input('Digite o numero%d: ' % (i+1))))
for i in range(0,n,1):
    b.append(int(input('Digite o numero%d: ' % (i+1))))
for i in range(0,n,1):
    c.append(int(input('Digite o numero%d: ' % (i+1))))
print (crescente(a))
print (decrescente(a))
print (igualdade(a))
print (crescente(b))
print (decrescente(b))
print (igualdade(b))
print (crescente(c))
print (decrescente(c))
print (igualdade(c))






