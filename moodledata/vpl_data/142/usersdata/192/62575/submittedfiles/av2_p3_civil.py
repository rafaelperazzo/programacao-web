# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def somaA(x,y):
    mx= media (x)
    my= media (y)
    soma= 0
    for i in range (0, len(x), 1):
        soma = soma + ((x [i]-mx)*(y[i]-my))
    return (soma)
def soma(a):
    m=media(a)
    soma=0
    for i in range (0, len(a), 1):
        soma=soma+((a[i]-m))**2
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

p= somaA(x)/((soma(x)*soma(y))**((0.5))

p = abs(p)

print('%.4f' % p)
