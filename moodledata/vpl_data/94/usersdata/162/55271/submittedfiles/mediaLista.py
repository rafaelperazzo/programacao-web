# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de valores:'))
lista=[]
for i in range(0,n,1):
    a=float(input('Digite o valor:'))
    lista.append(a)
def  media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    return(media)
print('%.2f' %media(lista))    
print('%.2f' %lista[0])
print('%.2f' %(len(lista)-1))