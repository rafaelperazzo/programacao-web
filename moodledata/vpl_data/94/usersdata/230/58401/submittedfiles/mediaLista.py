# -*- coding: utf-8 -*-
def media(lista):
    soma=0
    for i in range (0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    return(media)

n=int(input('Digite quantidade de valores: '))
a=[]   
for i in range (0,n,1):
    valor=int(input('Digite valor: '))
    a.append(valor)

print('%.2f' %a[0])
print('%.2f' %len(a))
print('%.2f' %media(a))
print(a)
