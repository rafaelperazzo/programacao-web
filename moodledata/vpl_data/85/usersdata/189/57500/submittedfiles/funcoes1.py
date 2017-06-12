# -*- coding: utf-8 -*-

def crescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

n=int(input('digite n:'))
a=[]
for i in range(0,n+1,1):
    numero=int(input('digite n:'))
    a.append(numero)
if crescente(a)==True:
    print('S')
else:
    print('N')

