# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def soma1(x,y):
    medx=media(x)
    medy=media(y)
    cont=0
    for i in range(0,len(x),1):
        cont=cont+((x[i]-medx)*(y[i]-medy))
    return cont

        


  
def entradaLista(n):
    a = []
    for i in range(0,n,1):
        valor = float(input('Digite um valor: '))
        a.append(valor)
    return (a)

n = int(input('Digite o tamanho da lista: '))
x = entradaLista(n)
y = entradaLista(n)

p =soma1(x,y)/(somaD(x)*somaD(y))**0.5

p = abs(p)

print('%.4f' % p)
