# -*- coding: utf-8 -*-

def crescente(lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i]:
            cont=cont+1
            return(True)
        else:
            return(False)

#escreva as demais funções
            
def descrescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i]:
            cont=cont+1
            return(True)
        else:
            return(False)
    
def iguais(n,m,r):
    if a[i]==b[i] or a[i]==c[i] or b[i]==c[i]:
        return(True)
    else:
        return(False) 
#escreva o programa principal
n=int(input('Digite a quantidade de elementos da lista 1:'))
m=int(input('Digite a quantidade de elementos da lista 2:'))
r=int(input('Digite a quantidade de elementos da lista 3:'))
a=[]
for i in range(1,n+1,1):
    valor1=int(input('Digite o elemento da lista 1:'))
    a.append(valor1)


b=[]
for i in range(1,m+1,1):
    valor2=int(input('Digite o elemento da lista 2:'))
    b.append(valor2)
    

c=[]
for i in range(1,r+1,1):
    valor3=int(input('Digite o elemento da lista 3:'))
    c.append(valor3)
    
    
if crescente(a):
    print('S')
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
    
if a[i]==b[i] or a[i]==c[i] or b[i]==c[i]:
    print('S')
else:
    print('N')
