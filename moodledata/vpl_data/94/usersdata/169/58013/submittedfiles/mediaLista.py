# -*- coding: utf-8 -*-
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    média=soma/len(lista)
    return média

n=int(input('Digite a Quantidade de Números:'))
l1=[]
for i in range(1,n+1,1):
    v=float(input('Digite o Valores de Inteiros da Lista:'))
    l1.append(v)
print('%.2f' %l1[0])
print('%.2f' %l1[len(l1)-1])
print('%.2f' %média(l1))
print(l1)




