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
        soma=soma+((a[i]-media)**2)
    desvpadrao=(soma/(n-1))**0.5
    return desvpadrao
n=int(input('tamanho da lista a:'))
a=[]
for i in range(1,n+1,1):
    valor=float(input('Digite o valor: '))
    a.append(valor)
n=int(input('Digite o tamanho da lista 2: '))
b=[]
for i in range(1,n+1,1):
    x=float(input(' valo 2: '))
    b.append(x)

print('%.2f' %media(a))
print('%.2f' %desvpadra(a,media(a)))
print('%.2f' %media(b))
print('%.2f' %desvpadra0(b,media(b)))
    