# -*- coding: utf-8 -*-

def pico(l):
    if l[0]<l[1]:
        cont=1
        i=0
        while cont<n:
            if i==0:
                if l[cont]<l[cont-1]:
                    i=1
            elif i==1:
                if l[cont]>l[cont-1]:
                        i=2
            else:
                return(2)
            cont=cont+1
        return(1)
    else:
        return(2)

n =int(input('Digite a quantidade de elementos da lista:'))
a=[]
i=0
while i<n:
    valor=int(input('digite valor:'))
    a.append(valor)
    i=i+1
if pico(a)==1:
    print('S')
else:
    print('N')