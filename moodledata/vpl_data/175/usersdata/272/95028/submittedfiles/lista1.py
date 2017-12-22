# -*- coding: utf-8 -*-

n=int(input('Digite o número de elementos da lista: '))
a=[]
for i in range (0,n,1):
    a.append(int(input('Digite o valor: ')))

soma_par=0
soma_impar=0
cont_par=0
cont_impar=0
for i in range (0,len(a),1):
    if (a[i]%2==0):
        soma_par=soma_par+i+1
        cont_par=cont_par+1
    elif (a[i]%2==1):
        soma_impar=soma_impar+i+1
        cont_impar=cont_impar+1
print(soma_impar)
print(soma_par)
print(cont_impar)
print(cont_par)
print(a)