# -*- coding: utf-8 -*-
def lecker(lista):
    f=len(lista)
    h=0
    
    if lista[0]>lista[1]:
        h+=1
    if lista[0]==lista[1]:
        h+=0
    if lista[f-1]>lista[f-2]:
        h+=1
    if lista[f-1]==lista[f-2]:
        h+=0
    
    for i in range (1, f-2, 1):
        if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
            h+=1
        if lista[i]==lista[i-1] or lista[i]==lista[i+1]:
            h+=0
    
    if h=1:
        return True
    if not h=1:
        return False

n=int(input('Digite o número de elementos das listas: '))
lista1=[]
lista2=[]

for i in range (0, n, 1):
    lista1.append(int(input('Digite o %dº elemento da 1ª lista: ' % (i+1))))
for i in range (0, n, 1):
    lista2.append(int(input('Digite o %dº elemento da 2ª lista: ' % (i+1))))

if lecker(lista1)==True:
    print('S')
if lecker(lista1)==False:
    print('N')
if lecker(lista2)==True:
    print('S')
if lecker(lista2)==False:
    print('N')