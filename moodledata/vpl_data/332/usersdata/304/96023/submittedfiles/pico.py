# -*- coding: utf-8 -*-
'''
def pico(lista):
    #CONTINUE...
    conta = 0
    contb = 0
    contc = 0
    for i in range(1,len(a),1):
        if(a[i]>a[i-1]) and contb==0:
            conta=conta+1
        elif(a[i]<a[i-1]):
            contb=contb+1
        else:
            contc=contc+1
            break
    if conta + contb == len(a)-1:
        return(True)
    else:
        return(False)
n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]
for i in range(0,n,1):
    v=int(input('Termo: '))
    a.append(v)
if pico(a)==True:
    print('S')
else:
    print('N')

'''
def crescente(lista):
    cont = 0
    for i in range(0,len(lista),1):
        if (i==0):
            if(lista[0]<lista[1]):
                cont = cont+1
        elif i == len(lista)-1:
            if lista[len(lista)-2] <lista[len(lista)-1]:
                cont = cont + 1
        else:
            if lista [i-1]<lista[i]<lista[i+1]:
                cont = cont + 1
    if cont == len(lista):
        return(True)
    else:
        return(False)
        
def decrescente(lista):
    cont = 0
    for i in range(0,len(lista),1):
        if (i==0):
            if(lista[0]>lista[1]):
                cont = cont+1
        elif i == len(lista)-1:
            if lista[len(lista)-2]>lista[len(lista)-1]:
                cont = cont + 1
        else:
            if lista [i-1]>lista[i]>lista[i+1]:
                cont = cont + 1
    if cont == len(lista):
        return(True)
    else:
        return(False)
        
def pico(lista):
    e_max = max(lista)
    i_max = lista.index(e_max)
    for i in range (0,i_max+1,1):
        e_ant = lista[i]
        ant = []
        ant.append(e_ant)
    for i in range (i_max+1,len(lista),1):
        e_post = lista[i]
        post = []
        post.append(e_post)
    if crescente(ant) and decrescente(post):
        return(True)
    else:
        return(False)
n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
a = []
for i in range(0,n,1):
    a1 = float(input('Elemento a: '))
    a.append(a1)
if pico(a):
    print('S')
else:
    print('N')
    '''