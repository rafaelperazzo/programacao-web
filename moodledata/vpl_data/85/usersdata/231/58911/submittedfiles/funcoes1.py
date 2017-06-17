# -*- coding: utf-8 -*-

def crescente(lista):
    for i in range(0,len(lista),1):
        if lista[i]<=(lista[i-1]:
            return False
        else:
            return True
            
    #escreva o código da função crescente aqui
def decrescente(lista):
    for i in  range(0,len(lista),1):
        if lista[i]>=(lista[i]+1):
            return True 
        else:
            return False
def iguais(lista):
    for i in range(0,len(lista),1):
        if lista[i]!=(lista[i]+1):
            return False
        else:
            return True 
a=[]
b=[]
c=[]
n=int(input('digite n:'))
for i in range(0,n,1):
    valor=int(input('digite valores a:'))
    a.append(valor)
for i in range(0,n,1):
    valor=int(input('digite valores b:'))
    b.append(valor)
for i in range(0,n,1):
    valor=int(input('digite valores c:'))
    c.append(valor)

if crescente(a)==True:
    print('S')
else:
    print('N')
if decrescente(a)==True:
    print('S')
else:
    print('N')
if iguais(a)==True:
    print('S')
else:
    print('N')
if crescente(b)==True:
    print('S')
else:
    print('N')
if decrescente(b)==True:
    print('S')
else:
    print('N')
if iguais(b)==True:
    print('S')
else:
    print('N')
if crescente(c)==True:
    print('S')
else:
    print('N')
if decrescente(c)==True:
    print('S')
else:
    print('N')
if iguais(c)==True:
    print('S')
else:
    print('N')
#escreva as demais funções





#escreva o programa principal
