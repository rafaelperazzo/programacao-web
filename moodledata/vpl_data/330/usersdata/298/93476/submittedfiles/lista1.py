# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de valores: '))

lista=[]
for i in range (0, n, 1):
    lista.append(int(input('Digite um valor para a lista: ')))

somaimpar=0
qntdimpar=0
for i in range (0, n, 1):
    if lista[i]%2==1:
        somaimpar+=lista[i]
        qntdimpar+=1

somapar=0
qntdpar=0
for i in range (0, n, 1):
    if lista[i]%2==0:
        somapar+=lista[i]
        qntdpar+=1
        
print(somaimpar)
print(somapar)
print(qntdimpar)
print(qntdpar)
print(lista)