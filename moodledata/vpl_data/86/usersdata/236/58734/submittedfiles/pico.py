# -*- coding: utf-8 -*-

def pico(lista):
    i=1
    cont1=0
    cont2=0
    while lista[i]>lista[i-1]:
        i=i+1
        cont1=cont1+1
    while lista[i]<lista[i-1]:
        i=i+1
        cont2=cont2+1
    if cont1+cont2==(len(lista)-1):
        print('S')
        return True
    else:
        print('N')
        return False
        

n = int(input('Digite a quantidade de elementos da lista: '))
A=[]
for i in range (1,n+1,1):
    numero= float(input('numero:'))
    A.append (numero)


  

