# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)
def soma1(x,y):
    a = media(x)
    b = media(y)
    soma = 0
    for i in range(0,len(x),1):
        soma = soma+((x[i]-a)*(y[i]-b))
    return(soma)
def soma2(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma+((a[i]-media(a))**2)
    return(soma)
  
def entradaLista(n):
    a = []
    for i in range(0,n,1):
        valor = float(input('Digite um valor: '))
        a.append(valor)
    return (a)

n = int(input('Digite o tamanho da lista: '))
x = entradaLista(n)
y = entradaLista(n)

p = 

p = abs(p)

print('%.4f' % p)
