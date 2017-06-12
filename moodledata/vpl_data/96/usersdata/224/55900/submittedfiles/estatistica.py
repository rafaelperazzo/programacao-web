# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvpadrao(lista,media):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media)**2)
    desvpadrao=(soma/(n-1))**0.5
    return desvpadrao
n=int(input('tamanho da lista a:'))
a=[]
for i in range(1,n+1,1):
    valor=float(input('valor1: '))
    a.append(valor)
n=int(input('Digite o tamanho da lista 2: '))
b=[]
for i in range(1,n+1,1):
    x=float(input(' valor 2: '))
    b.append(x)
m1=media(a)
m2=media(b)
d1=desvádrao(a)
d2=desvpadrao(b)
print('%.2f' %m1)
print('%.2f' %d1)
print('%.2f' %m2)
print('%.2f' %d2)
    