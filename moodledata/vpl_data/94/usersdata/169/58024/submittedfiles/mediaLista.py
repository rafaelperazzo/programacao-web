# -*- coding: utf-8 -*-
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado

n=int(input('Digite a Quantidade de Números:'))
l1=[]
for i in range(0,n,1):
    v=int(input('Digite o Valores da Lista:'))
    l1.append(v)
print('%.2f' %l1[0])
print('%.2f' %l1[len(l1)-1])
print('%.2f' %media(l1))
print(l1)




