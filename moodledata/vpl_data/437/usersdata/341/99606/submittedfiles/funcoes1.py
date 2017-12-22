# -*- coding: utf-8 -*-

 #escreva o código da função crescente aqui
def crescente (lista):
    c=0
    for i in range (0, n-1, 1):
        w=i+1
        if lista[i] < lista[w]:
            c=c+1
    if c==(n-1):
        print('S')
    else:
        print('N')
            
#escreva as demais funções
def decrescente (lista):
    c=0
    for i in range(0, n-1, 1):
        w=i+1
        if lista[i] > lista[w]:
            c=c+1
    if c==(n-1):
        print('S')
    else:
        print('N')
        
def v1_consecutivos (lista):
    c=0
    for i in range (0, n-1, 1):
        if lista[i]==lista[i+1]:
            c=c+1
    if c!=0:
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
    
crescente(a)
decrescente(a)
v1_consecutivos(a)

crescente(b)
decrescente(b)
v1_consecutivos(b)

crescente(c)
decrescente(c)
v1_consecutivos(c)
    
        
    