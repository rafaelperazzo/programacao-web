# -*- coding: utf-8 -*-

def crescente(lista):
    contd=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<(lista[i+1]):
            contd=contd+1
    if (contd)==len(lista)-1:
        return True
    else:
        return False
            
    #escreva o código da função crescente aqui
def decrescente(lista):
    contc=0
    for i in  range(0,len(lista)-1,1):
        if lista[i]>(lista[i+1]):
            contc=contc+1
    if contc==len(lista)-1:
        return False 
    else:
        return True
def iguais(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==(lista[i+1]):
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False 
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

if crescente(a):
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
