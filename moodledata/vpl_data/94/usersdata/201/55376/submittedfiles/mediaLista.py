# -*- coding: utf-8 -*-
LISTA=[]
n=int(input('Digite n:'))
for i in range(1,n+1,1):
    valor=float(input('valor'))
    LISTA.append(valor)
soma=0
for i in range(0,len(LISTA),1):
    soma=soma+LISTA[i]
media=soma/len(LISTA)
print('%.2f' %LISTA[0])
print('%.2f' %LISTA[n-1])
print('%.2f' %media)
print(LISTA)