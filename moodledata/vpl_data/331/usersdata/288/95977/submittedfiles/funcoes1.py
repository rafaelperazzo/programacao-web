# -*- coding: utf-8 -*-

def crescente (lista1):
    #escreva o código da função crescente aqui
    cont_crescente=0
    for i in range (0,n-1,1):
        if lista1[i]<(lista1[i+1]):
            cont_crescent+=1
    if cont_crescente==len(lista1)-1:
        return True
    else:
        return False
        
def crescente (lista2):
    cont_crescente=0
    for i in range (0,n-1,1):
        if lista2[i]<(lista2[i+1]):
            cont_crescent+=1
    if cont_crescente==len(lista2)-1:
        return True
    else:
        return False
        
def crescente (lista3):
    cont_crescente=0
    for i in range (0,n-1,1):
        if lista3[i]<(lista3[i+1]):
            cont_crescent+=1
    if cont_crescente==len(lista3)-1:
        return True
    else:
        return False

#escreva as demais funções
def decrescente (lista1):
    cont_decrescente=0
    for i in range (0,n-1,1):
        if lista1[i]>(lista1[i+1]):
            cont_decrescent+=1
    if cont_decrescente==len(lista1)-1:
        return True
    else:
        return False
            
def decrescente (lista2):
    cont_decrescente=0
    for i in range (0,n-1,1):
        if lista2[i]>(lista2[i+1]):
            cont_decrescent+=1
    if cont_decrescente==len(lista2)-1:
        return True
    else:
        return False
            
def decrescente (lista3):
    cont_decrescente=0
    for i in range (0,n-1,1):
        if lista3[i]>(lista3[i+1]):
            cont_decrescent+=1
    if cont_decrescente==len(lista3)-1:
        return True
    else:
        return False

def consecutivo (lista1):
    cont_consecutivo=0
    for i in range (0,n,1):
        if lista1[i]>(lista1[i+1]):
            cont_consecutivo+=1
    if cont_consecutivo>0:
        return True
    else:
        return False
        

def consecutivo (lista2):
    cont_consecutivo=0
    for i in range (0,n,1):
        if lista2[i]>(lista2[i+1]):
            cont_consecutivo+=1
    if cont_consecutivo>0:
        return True
    else:
        return False
        

def consecutivo (lista3):
    cont_consecutivo=0
    for i in range (0,n,1):
        if lista3[i]>(lista3[i+1]):
            cont_consecutivo+=1
    if cont_consecutivo>0:
        return True
    else:
        return False

#escreva o programa principal
n=int(input('Digite a quantidade de elementos das tres listas: '))
lista1=[]
for i in range (0,n,1):
    lista1.append(int(input('Digite um valor %d para a lista_1: '%(i+1))))
lista2=[]
for i in range (0,n,1):
    lista2.append(int(input('Digite um valor %d para a lista_2: '%(i+1))))
lista3=[]
for i in range (0,n,1):
    lista3.append(int(input('Digite um valor %d para a lista_3: '%(i+1))))
if crescente (lista1):
    print ('S')
else:
    print ('N')
if crescente (lista2):
    print ('S')
else:
    print ('N')
if crescente (lista3):
    print ('S')
else:
    print ('N')
if decrescente (lista1):
    print ('S')
else:
    print ('N')
if decrescente (lista2):
    print ('S')
else:
    print ('N')
if decrescente (lista3):
    print ('S')
else:
    print ('N')
if consecutivo (lista1):
    print ('S')
else:
    print ('N')
if consecutivo (lista2):
    print ('S')
else:
    print ('N')
if consecutivo (lista3):
    print ('S')
else:
    print ('N')