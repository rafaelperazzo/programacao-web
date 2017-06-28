# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

def soma1(h,m):
    mh=media(h)
    mm=media(m)
    soma=0
    for i in range(0,len(h),1):
        soma=soma+((h[i]-mh)*(m[i]-mm))
        return(soma)

def somaC(lista):
    mlista=media(lista
    soma=0
    for i in range (0,len(lista),1):
        soma=soma+(lista[i]-mlista)**2
        return(h)
        
def entradaLista(n):
    a = []
    for i in range(0,n,1):
        valor = float(input('Digite um valor: '))
        a.append(valor)
    return (a)

n = int(input('Digite o tamanho da lista: '))
x = entradaLista(n)
y = entradaLista(n)


p =soma1(x,y)/(somaC(x)*somaC(y))**0.5
p= abs(p)

print('%.4f' % p)
