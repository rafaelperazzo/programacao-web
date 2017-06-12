# -*- coding: utf-8 -*-
l=[]
n = int(input('Digite a quantidade de valores: '))
for i in range(0,n,1):
    termo=int(input('Digite o valor de índice '+str(i)+' da lista: '))
    l.append(termo)
    
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    return(media)
    
print(l[0])
print(l[len(l)-1])
print(media(l))
print(l)

