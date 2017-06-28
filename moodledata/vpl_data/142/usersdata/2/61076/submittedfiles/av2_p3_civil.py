# -*- coding: utf-8 -*-
def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

def dif(a):
    soma = 0
    m = media(a)
    for i in range(0,len(a),1):
        soma = soma + (a[i]-m)**2
    return (soma)

def somaN(a,b):
    soma = 0
    ma = media(a)
    mb = media(b)
    for i in range(0,len(a),1):
        soma = soma + ((a[i]-ma)*(b[i]-mb))
    return (soma)
    
def entradaLista(n):
    a = []
    for i in range(0,n,1):
        valor = float(input('Digite um valor: '))
        a.append(valor)
    return (a)

n = int(input('Digite o tamanho da lista: '))
x = entradaLista(n)
y = entradaLista(n)
p = somaN(x,y)/((dif(x)*dif(y))**(0.5))
print (abs(p))


