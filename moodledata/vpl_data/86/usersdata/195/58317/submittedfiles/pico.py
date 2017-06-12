# -*- coding: utf-8 -*-
def pico(lista):
    a=(len(lista)+1)//2
    b=a-1
    for i in range(1,a,1):
        if lista[i]<lista[i-1]:
            return False
    return True 
n=int(input('digite a quantidade de elementos da lista:'))
lista=[]
for i in range (1,n+1,1):
    a=int(input('digite a :'))
    lista.append(a)
cont=0
for i in range(1,len(lista),1):
    if lista[i]==lista[i-1]:
        cont=cont+1
if cont==0:
    if pico(lista):
        print('S')
    else:
        print('N')
else:
    print('N')



