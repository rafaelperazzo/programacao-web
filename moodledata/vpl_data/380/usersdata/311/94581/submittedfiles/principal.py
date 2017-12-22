# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=[1,2,3]
n=int(input('Digite seu numero: '))
if max(a)==a[2]:
    print ('True')
def crescente(lista):
    for i in range (0,n,1):
        while lista[i]<lista[i+1]:
            return True
print (crescente(a))