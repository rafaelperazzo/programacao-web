# -*- coding: utf-8 -*-

def crescente (a):
    #escreva o código da função crescente aqui
    cont = 0
    for i in range(1, len(a), 1):
        if (a[i]>a[i-1]):
            cont = cont + 1
        else:
            break
        if cont == len(a) - 1:
            return(True)
        else:
            return(False)

#escreva as demais funções

def decrescente (a):
    cont = 0
    for i in range(1, len(a), 1):
        if (a[i]<a[i-1]):
            cont = cont + 1
        else:
            break
        if cont == len(a) - 1:
            return(True)
        else:
            return(False)

def consecutivo (a):
    cont = 0
    for i in range(1, len(a), 1):
        if (a[i]==a[i-1]):
            break
        else:
            cont = cont + 1
        if cont == len(a) - 1:
            return(False)
        else:
            return(True)

#escreva o programa principal

n=int(input('n: '))
a=[]
b=[]
c=[]

for i in range(0,n,1):
    v_a=int(input('a: '))
    a.append(v_a)
for i in range(0,n,1):
    v_b=int(input('b: '))
    b.append(v_b)
for i in range(0,n,1):
    v_c=int(input('c: '))
    c.append(v_c)
    
if crescente(a) == True:
    print('S')
if crescente(a) == False:
    print('N')
if decrescente(a) == True:
    print('S')
if decrescente(a) == False:
    print('N')
if consecutivo(a) == True:
    print('S')
if consecutivo(a) == False:
    print('N')
    
if crescente(b) == True:
    print('S')
if crescente(b) == False:
    print('N')
if decrescente(b) == True:
    print('S')
if decrescente(b) == False:
    print('N')
if consecutivo(b) == True:
    print('S')
if consecutivo(b) == False:
    print('N')
    
if crescente(c) == True:
    print('S')
if crescente(c) == False:
    print('N')
if decrescente(c) == True:
    print('S')
if decrescente(c) == False:
    print('N')
if consecutivo(c) == True:
    print('S')
if consecutivo(c) == False:
    print('N')
    