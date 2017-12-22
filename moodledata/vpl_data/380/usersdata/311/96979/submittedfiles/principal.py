# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=[]
def crescente(lista):
    for i in range (0,n,1):
        while lista[i]<lista[i+1]:
            return 'S'
        else:
            return 'N'

n= int(input('Digite a quantidade abaixo: '))
for i in range (0,n,1):
    a.append(int(input('Digite o numero%d: ' %(i+1))))
print (crescente(a))

