# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

def somaA(a,b):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+(a[i]-media(a))*(b[i]-media(b))
    return(soma)
def somaD(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
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

p = somaA(x,y)/((somaD(x)*somaD(y))**(0.5))

p = abs(p)

print('%.4f' % p)
