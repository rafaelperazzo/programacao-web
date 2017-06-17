# -*- coding: utf-8 -*-

def crescente (lista):
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            return True
        return False
        
def decrescente (lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            return False
        return True
        
def numiguais(lista):
    for i in range(o,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            return True
    return False

n=int(input('Digite a quantidade de elementos:'))
a=[]
b=[]
c=[]
    
for i in range(0,n,1):
    x=float(input('Digite os elementos:'))
    a.append(x)
for i in range(0,n,1):
    y=float(input('Digite os elementos:'))
    b.append(y)
for i in range(0,n,1):
    w=float(input('Digite os elementos:'))
        
        
#escreva as demais funções
n=int(input('Quantidade de elementos: '))

a=[]
b=[]
c=[]

for i in range(1,n+1,1):
    a.append(input('Lista A - %d° Valor: '%i))
for i in range(1,n+1,1):
    b.append(input('Lista B - %d° Valor: '%i))
for i in range(1,n+1,1):
    c.append(input('Lista C - %d° Valor: '%i))
    
    
    
def teste(a):
    if crescente(a):
        print ('S')
    else:
        print ('N')
    if decrescente(a):
        print ('S')
    else:
        print ('N')
    if consecutivos(a):
        print ('S')
    else:
        print ('N')
        

teste(a)
teste(b)
teste(c)






#escreva o programa principal
