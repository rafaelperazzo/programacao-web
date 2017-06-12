# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de valores:'))
lista=[]
soma=0
def  media(lista):
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    return(media)
print('%.2f' %media)    
print('%.2f' %lista[0])
print('%.2f' %(len(lista)-1))