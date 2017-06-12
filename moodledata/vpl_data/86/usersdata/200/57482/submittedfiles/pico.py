# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    if a[0]<a[1]:(
        cont=1
        i=0
        while cont<n:
            if i==0:
                if a[cont]<a[cont-1]:
                    i=1
                elif i==1:
                    if a[cont]>a[cont-1]:
                        i=2
                    else:
                        return(2)
                    cont=cont+1
        return(1)
    else:
        return(2)
n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]
i=0
while i<n:
    v=int(input('Coloque um numero:'))
    a.append(v)
    i=i+1
if pico(a)==1:
    print('S')
else:
    print('N')
