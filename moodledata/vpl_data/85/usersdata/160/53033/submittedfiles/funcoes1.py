# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i]:
            cont=cont+1

#escreva as demais funções
            
def descrescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i]:
            cont=cont+1


#escreva o programa principal
n=int(input('Digite a quantidade de elementos da lista:'))
a=[]
for i in range(1,n+1,1):
    valor1=float(input('Digite o elemento da lista:'))
    a.append(valor1)
    
b=[]
for i in range(1,n+1,1):
    valor2=float(input('Digite o elemento da lista:'))
    b.append(valor2)
    
c=[]
for i in range(1,n+1,1):
    valor3=float(input('Digite o elemento da lista:'))
    c.append(valor3)
    
    
if crescente(a):
    print('S')
    print('N')
else:
    print('N')
    
if descrescente(a):
    print('S')
    
else:
    print('N')
    

if crescente(b):
    print('S')
    
else:
    print('N')
    
if descrescente(b):
    print('S')
    
else:
    print('N')
    
    
if crescente(c):
    print('S')
    
else:
    print('N')
    
if descrescente(c):
    print('S')
    
else:
    print('N')
