# -*- coding: utf-8 -*-
def funçao(lista):
    cont=0
    cont2=0
    soma2=0
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2!=0:
            cont=cont+1
            soma=soma+lista[i]
        else:
            soma2=soma2+1
            cont2=cont2+1
    return cont
    return cont2
    return soma
    return soma2
n=int(input('Digite o tamanho da lista: '))

a=[]
for i in range(1,n+1,1):
    numero=int(input('Digite o numero: '))
    a.append(numero)

print(funçao(a))
print(a)