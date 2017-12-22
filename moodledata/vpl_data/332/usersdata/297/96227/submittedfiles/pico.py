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
    for i in range(0,cresc,1) :
        del lista[i]
    decresc=0
    print(cresc)
    g=n-cresc
    print(len(lista))
    print(g)
    print(lista)
    if g>1:
        for i in range(g-1,0,-1):
            if lista[i]<lista[i+1]:
                decresc=decresc+1
            else:
                break
    for i in range(0,decresc,1):
        del lista[i]
    r=g-decresc
    if r>1:
        for i in range(0,r-1,1):
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
