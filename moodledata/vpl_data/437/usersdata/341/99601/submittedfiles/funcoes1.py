# -*- coding: utf-8 -*-

 #escreva o código da função crescente aqui
def crescente (lista):
    k=0
    for i in range (0, n-1, 1):
        p=i+1
        if lista[i] < lista[p]:
            k=k+1
    if k==(n-1):
        print('S')
    else:
        print('N')
            
#escreva as demais funções
def decrescente (lista):
    k=0
    for i in range(0, n-1, 1):
        p=i+1
        if lista[i] > lista[p]:
            k=k+1
    if k==(n-1):
        print('S')
    else:
        print('N')
        
def v1_consecutivos (lista):
    k=0
    for i in range (0, n-1, 1):
        if lista[i]==lista[i+1]:
            k=k+1
    if k!=0:
        print('S')
    else:
        print('N')
#escreva o programa principal
n = int(input('Digite o valor de n: '))
a=[]
for i in range (0, n, 1):
    a.append(int(input('Digite o valor da Lista A: ')))
    
b=[]
for i in range (0, n, 1):
    b.append(int(input('Digite o valor da Lista B: ')))
    
c=[]
for i in range (0, n, 1):
    c.append(int(input('Digite o valor da Lista C: ')))
    
        
    