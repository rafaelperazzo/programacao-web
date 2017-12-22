# -*- coding: utf-8 -*-
n=3
lista=[1,2,3]
def pico(lista):
    #CONTINUE...
    cresc=0
    igual=0
    for i in range(0,n-1,1):
        if lista[i]<lista[i+1]:
            cresc=cresc+1
        else :
            break
    decresc=0
    g=int(lista[i])
    for i in range(g-1,n-1,1):
        if lista[i]>lista[i+1]:
            decresc=decresc+1
        else:
            break
    v=lista[i]
    if cresc+decresc!=n :
        for i in range(g,v,1):
            if lista[i]<lista[i+1]:
                igual=igual+1
            else :
                igual=igual+1
    if cresc>0 and decresc>0 and igual==0:
        return True
    else :
        return False
n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
a=[]
for i in range(0,n,1) :
    a.append(int(input('adicione um elemento a lista a: ')))
lista=a
if pico(a):
    print('S')
else:
    print('N')
