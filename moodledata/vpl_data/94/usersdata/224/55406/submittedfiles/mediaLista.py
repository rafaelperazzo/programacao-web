# -*- coding: utf-8 -*-
def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    return media
n=int(input('Digite o tamanho da lista: '))
m=[]
for i in range(1,n+1,1):
    valor=int(input('Digite os valores da lista: '))
    m.append(valor)
print('%.2f' %a[0])
print('%.2f' %a[len(a)])
print('%.2f' %media[a])
print(a)
