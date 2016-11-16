# -*- coding: utf-8 -*-
from __future__ import division

def crescente (a):
    #escreva o código da função crescente aqui
    cont1=0
    for i in range(0,len(a)-1,1):
        if a[i]<a[i+1]:
            cont1=cont1+1
    if cont1==len(a)-1:
        return True
    else:
        return False

#escreva as demais funções

def decrescente(a):
    cont2=0
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            cont2=cont2+1
    if cont2==len(a)-1:
        return True
    else:
        return False

def iguais(a):
    cont3=0
    for i in range(0,len(a)-1,1):
        if a[i]==a[i+1]:
            cont3=cont3+1
    if cont1!=0:
        return True
    else:
        return False


#escreva o programa principal

n=input('Digite a quantidade de termos: ')

a=[]
b=[]
c=[]

for i in range(0,n,1):
    a.append(input('Digite um termo de A: '))
for i in range(0,n,1):
    b.append(input('Digite um termo de B: '))
for i in range(0,n,1):
    c.append(input('Digite um termo de C: '))

if crescente(a):
    print 'S'
else:
    print 'N'

if decrescente(a):
    print 'S'
else:
    print 'N'

if iguais(a):
    print 'S'
else:
    print 'N'

if crescente(b):
    print 'S'
else:
    print 'N'

if decrescente(b):
    print 'S'
else:
    print 'N'

if iguais(b):
    print 'S'
else:
    print 'N'

if crescente(c):
    print 'S'
else:
    print 'N'

if decrescente(c):
    print 'S'
else:
    print 'N'

if iguais(c):
    print 'S'
else:
    print 'N'