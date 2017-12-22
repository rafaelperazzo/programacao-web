# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    if lista[0]<lista[1]<lista[2]<lista[3]<lista[4]:
        return True
    else:
        return False
#escreva as demais funções
def decrescente (lista):
    if lista[0]>lista[1]>lista[2]>lista[3]>lista[4]:
        return True
    else:
        return False
        
def consecutivo(lista):
    if lista[0]==lista[1] or lista[1]==lista[2] or lista[2]==lista[3] or lista[3]==lista[4]:
        return True
    else:
        return False

#escreva o programa principal
n = int(input('Digite a quantidade de elementos das listas: '))
a = []
b = []
c = []
for i in range(0,n,1):
    a.append(int(input('Digite um elemento de a: ')))
for i in range(0,n,1):
    b.append(int(input('Digite um elemento de b: ')))
for i in range(0,n,1):
    c.append(int(input('Digite um elemento de c: ')))    

if crescente(a):
    print('S')
else:
    print('N')
if decrescente(a):
    print('S')
else:
    print('N')
if consecutivo(a):
    print('S')
else:
    print('N')    
    
if crescente(b):
    print('S')
else:
    print('N')
if decrescente(b):
    print('S')
else:
    print('N') 
if consecutivo(b):
    print('S')
else:
    print('N')        
    
if crescente(c):
    print('S')
else:
    print('N')
if decrescente(c):
    print('S')
else:
    print('N')
if consecutivo(c):
    print('S')
else:
    print('N')        

