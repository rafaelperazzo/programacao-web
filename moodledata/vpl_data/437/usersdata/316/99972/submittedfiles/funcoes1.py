# -*- coding: utf-8 -*-
n=int(input('digite o numero de elementos da lista:'))
lista1=[]
for i in range(0,n,1):
    lista1.append(float(input('digite o valor%d:' %(i+1))))
print(lista1)

n=int(input('digite o numero de elementos da lista:'))
lista2=[]
for i in range(0,n,1):
    lista2.append(float(input('digite o valor%d:' %(i+1))))
print(lista2)

n=int(input('digite o numero de elementos da lista:'))
lista3=[]
for i in range(0,n,1):
    lista3.append(float(input('digite o valor%d:' %(i+1))))
print(lista3)

def main(x):
    if crescente(lista1):
        print('S')
    else:
        print('N')
    
    


