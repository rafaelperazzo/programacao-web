# -*- coding: utf-8 -*-
n=int(input('digite o número de elementos:'))
lista1=[]
lista2=[]
lista3=[]
for i in range(0,n+1,1):
    elemento1=int(input('digite o elemento'))
    lista1.append(elemento1)

for i in range(0,n+1,1):
    elemento2=int(input('digite o elemento'))
    lista2.append(elemento2)

for i in range(0,n+1,1):
    elemento3=int(input('digite o elemento'))
    lista3.append(elemento3)

def crescente(a):
    
    for i in range(0,len(a),1):
        if a[i]<a[i+1]:
            return True
        else:
            return False
            
def decrescente(a):
    
    for i in range(0,len(a),1):
        if a[i]>a[i+1]:
            return True
        else:
            return False    
    
def elementosiguais(a):
    
    for i in range(0,len(a),1):
        if a[i]==a[i+1]:
            return True
        else:
            return False
    
if crescent(lista1):
    print('S')
if crescent(lista1)==False:
    print('N')    
if decrescente(lista1):
    print('S')
if decrescente(lista1)==False:
    print('N')    
if elementosiguais(lista1):
    print('S')
if elementosiguais(lista1)==False:
    print('N')
    
if crescent(lista2):
    print('S')
if crescent(lista2)==False:
    print('N')    
if decrescente(lista2):
    print('S')
if decrescente(lista2)==False:
    print('N')    
if elementosiguais(lista2):
    print('S')
if elementosiguais(lista2)==False:
    print('N')

if crescent(lista3):
    print('S')
if crescent(lista3)==False:
    print('N')    
if decrescente(lista3):
    print('S')
if decrescente(lista3)==False:
    print('N')    
if elementosiguais(lista3):
    print('S')
if elementosiguais(lista3)==False:
    print('N')    
