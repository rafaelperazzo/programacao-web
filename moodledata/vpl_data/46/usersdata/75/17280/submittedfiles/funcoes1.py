# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    for i in range (0,len(lista),1): #Você não vai até o último elemento da lista, pois o último não tem próximo
        if lista[i]<lista[i+1]:
            return True #Voce não pode retornar aqui!! Tem que contar, e fora da repetição verificar o contador.
        else:
            return False
            
def decrescente (lista): #mesmo comentário da função acima
    for i in range (0,len(lista),1):
        if lista[i]>lista[i+1]:
            return True
        else:
            return False
 
def consecutivos (lista):
    cont=0
    for i in range (0,len(lista),1): #não pode ir até o último, tem que ir até o penultimo, como nas funções acima
        if lista[i]==lista[i+1]:
            cont=cont+1
        
        if cont>0: #tem que ser fora da repetição
            return True
        else:
            return False
    
            
n=int(input('Digite o número de termos das listas:'))

a=[]
b=[]
c=[]

for i in range (0,n,1):
    a.append(input('Digite os valores da lista a:'))
    
for i in range (0,n,1):
    b.append(input('Digite os valores da lista b:'))
    
for i in range (0,n,1):
    c.append(input('Digite os valores da lista c:'))
    
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
    
    
if crescente(b):
    print ('S')
else:
    print ('N')
    
if decrescente(b):
    print ('S')
else:
    print ('N')
    
if consecutivos(b):
    print ('S')
else:
    print ('N')
    
    
if crescente(c):
    print ('S')
else:
    print ('N')
    
if decrescente(c):
    print ('S')
else:
    print ('N')
    
if consecutivos(c):
    print ('S')
else:
    print ('N')
    
