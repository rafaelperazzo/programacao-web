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
    valor1=int(input('Digite o elemento da lista:'))
    a.append(valor1)
    
b=[]
for i in range(1,n+1,1):
    valor2=int(input('Digite o elemento da lista:'))
    b.append(valor2)
    
c=[]
for i in range(1,n+1,1):
    valor3=int(input('Digite o elemento da lista:'))
    c.append(valor3)
    
    
if crescente(len(a)-1):
    print('S')
else:
    print('N')
    
if descrescente(len(a)-1):
    print('S')
    
else:
    print('N')
    

if crescente(len(b)-1):
    print('S')
    
else:
    print('N')
    
if descrescente(len(b)-1):
    print('S')
    
else:
    print('N')
    
    
if crescente(len(c)-1):
    print('S')
    
else:
    print('N')
    
if descrescente(len(c)-1):
    print('S')
    
else:
    print('N')
