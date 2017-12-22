# -*- coding: utf-8 -*-

def pico(lista):
    contcres=0
    contdecres=0
    for i in range(0,len(lista),1):
        if lista[i]<lista[i+1]:
            contcres=contcres+1
        else:
            break
    for i in range(contcres,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            contdecres=contdecres+1
        else:
            break
    if (contcres+contdecres==len(lista)-1 and contcresc>0 and contdecres>0):
        return('S')
    else:
        return('N')
    
n = int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(0,n,1):
    valorA=float(input('digite os valores da lista a: '))
    a.append(valorA)

print(pico(a))