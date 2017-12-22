# -*- coding: utf-8 -*-

def crescente (n,lista):
    #escreva o código da função crescente aqui
    cc = 0
    for i in range(0,n-1,1):
        if lista[i]<lista[i+1]:
            cc = cc + 1
    if cc == n-1:    
        return True
    else:
        return False
#escreva as demais funções
def decrescente (n,lista):
    dc = 0
    for i in range(0,n-1,1):
        if lista[i]>lista[i+1]:
            dc = dc + 1
    if dc == n-1:
        return True
    else:
        return False
        
def consecutivo(n,lista):
    ct = 0
    for i in range(0,n-1,1):
        if lista[i] == lista[i+1]:
            ct = ct + 1
    if ct > 0:   
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

if crescente(n,a):
    print('S')
else:
    print('N')
if decrescente(n,a):
    print('S')
else:
    print('N')
if consecutivo(n,a):
    print('S')
else:
    print('N')    
    
if crescente(n,b):
    print('S')
else:
    print('N')
if decrescente(n,b):
    print('S')
else:
    print('N') 
if consecutivo(n,b):
    print('S')
else:
    print('N')        
    
if crescente(n,c):
    print('S')
else:
    print('N')
if decrescente(n,c):
    print('S')
else:
    print('N')
if consecutivo(n,c):
    print('S')
else:
    print('N')        

