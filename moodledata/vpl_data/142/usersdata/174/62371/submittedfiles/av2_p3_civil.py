# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def somatorio(x,y):
    soma = 0
    for i in range(0,n,1):
        soma = soma+((x[i]-media(x))*(y[i]-media(y)))
    return (soma)

def somatorioxq(x):
    soma = 0
    for i in range(0,n,1):
        soma = soma + ((x[i]-media(x))**2)
    return (soma)

def somatorioyq(y):
    soma = 0
    for i in range(0,n,1):
        soma = soma + ((y[i]-media(y))**2)
    return (soma)
 # # # 
 
def entradaLista(n):
    a = []
    for i in range(0,n,1):
        valor = float(input('Digite um valor: '))
        a.append(valor)
    return (a)

n = int(input('Digite o tamanho da lista: '))
x = entradaLista(n)
y = entradaLista(n)

p = somatorio(x,y)/((somatorioxq(x)*somatorioyq(y))**0.5))

p = abs(p)

print('%.4f' % p)
