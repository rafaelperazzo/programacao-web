# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    n=3
    lista=[1,2,1]
    cresc=0
    igual=0
    decresc=0
    for i in range(0,n-1,1):
        if lista[i]<lista[i+1]:
            cresc=cresc+1
        else :
            break
    n=n-cresc
    for i in range(0,n,1) :
        if lista[i]>lista[i+1]:
            decresc=decresc+1
        else :
            break
    n=n-decresc
    for i in range(0,n,1):
        if lista[i]<lista[i+1]:
            igual=igual+1
        else :
            igual=igual+1
    if cresc>0 and descrec>0 and igual==0:
        return true
    else :
        return false
x = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
n=x
a=[]
lista=a
for i in range(0,x,1) :
    a.append(int(input('adicione um elemento a lista a: ')))
if pico(a):
    print('S')
else:
    print('N')
