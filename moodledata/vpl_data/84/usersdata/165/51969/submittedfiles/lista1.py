# -*- coding: utf-8 -*-

    
n=int(input('digite a quantidade de elementos:'))
lista=[]
for i in range(1,n+1,1):
    numero=int(input('digite um numero:'))
    lista.append(numero)
    
cont1=0
cont2=0
soma1=0
soma2=0    
for i in range(0,len(lista),1):
    if i%2!=0:
        cont1=cont1+1
        soma1=soma1+lista[i]
    else:
        cont2=cont2+1
        soma2=soma2+lista[i]

print(soma1)
print(soma2)
print(cont1)
print(cont2)
print(lista)
    
    
    
            

