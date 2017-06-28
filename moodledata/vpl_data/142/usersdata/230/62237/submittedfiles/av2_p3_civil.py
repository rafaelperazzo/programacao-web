# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def soma1(x,y):
    mediax=media(x)
    mediay=media(y)
    soma=0
    for i in range(0,len(x),1):
        soma=soma+((x[i]-mediax)*(y[i]-mediay))
    return soma

def soma2(lista):
    medlista=media(lista)
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-medlista)**2
    return soma

  
def entradaLista(n):
    a = []
    for i in range(0,n,1):
        valor = float(input('Digite um valor: '))
        a.append(valor)
    return (a)

n = float(input('Digite o tamanho da lista: '))
x = entradaLista(n)
y = entradaLista(n)

p = soma1(x,y)/((soma2(x)*soma2(y))*(0.5))

p = abs(p)

print('%.4f' % p)
