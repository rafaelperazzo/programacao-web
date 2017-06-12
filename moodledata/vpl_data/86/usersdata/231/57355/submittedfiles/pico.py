# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    for i in range(0,len(lista),1):
        if lista[i]>=lista[i+1]:
            return False
        if lista[i]<=lista[i+1]:
            return True


n = int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(0,n,1):
    b=int(input('b:'))
    a.append(b)
    if pico(b):
        print('S')
    else:
        print('N')

#CONTINUE...
