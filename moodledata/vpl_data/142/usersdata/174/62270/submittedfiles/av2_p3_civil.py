# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def somatorio(a,b):
    soma = 0
    for i in range(0,n,1):
        soma = soma+((a[i]-media(x))*(a[i]-media(y)))
    return (soma)

def somatorioqd(a,b):
    soma = 0
    for i in range(0,n,1):
        soma = soma+ (((a[i]-media(x))**2)*((a[i]-media(y))**2))
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

p = somatorio(a,b)/somatorioqd(a,b)

p = abs(p)

print('%.4f' % p)
