# -*- coding: utf-8 -*-
n=int(input('digite a quantidade termos da lista: '))
a=[]
contador_impar=0
contador_par=0
soma_impar=0
soma_par=0
for i in range (0,n,1):
    valor=int(input('digite os valores da lista: '))
    a.append(valor)
for i in range (0,len(a),1):
    if a[i]%2!=0:
        contador_impar=contador_impar+1
        soma_impar=soma_impar+a[i]
    else :
        contador_par=contador_par+1
        soma_par=soma_par+a[i]
print(soma_impar)
print(soma_par)
print(contador_impar)
print(contador_par)
print(a)


