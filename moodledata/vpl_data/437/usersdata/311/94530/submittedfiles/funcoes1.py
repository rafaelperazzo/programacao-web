# -*- coding: utf-8 -*-

def crescente(lista):
    #escreva o códintgo da função crescente aqui
    for i in range (0,n,1):
        if max(lista)==lista[n-1]:
            return 'S'
        else:
            return 'N'

#escreva as demais funções
def descrescente(lista):
    for i in range(0,n,1):
        if lista[i]>lista[i+1]:
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
n=int(input('Digite a quantidade: '))
for i in range(0,n,1):
    a.append(int(input('Digite o numero%d: ' % (i+1))))
for i in range(0,n,1):
    b.append(int(input('Digite o numero%d: ' % (i+1))))
for i in range(0,n,1):
    c.append(int(input('Digite o numero%d: ' % (i+1))))
print (crescente(a))
print (descrescente(a))
print (igualdade(a))
print (crescente(b))
print (descrescente(b))
print (igualdade(b))
print (crescente(c))
print (descrescente(c))
print (igualdade(c))




