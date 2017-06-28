# -*- coding: utf-8 -*-
def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    return (media)

def 1soma(x,y):
    mediax=media(x)
    mediay=media(y)
    soma=0
    for i in range(0,len(x),1):
        soma=soma+((x[i]-mediax)*(y[i]-mediay))
    return(soma)

def 2soma(lista):
    medial=media(lista)
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-medial)**2
    return(soma)

def entradaLista(n):
    a=[]
    for i in range(0,n,1):
        valor=float(input('Digite um valor: '))
        a.append(valor)
    return(a)

n=int(input('Digite o Tamanho da Lista:'))
x=entradaLista(n)
y=entradaLista(n)

p=1soma(x,y)/2soma(x)*2soma(y))
p = abs(p)

print('%.4f' % p)
