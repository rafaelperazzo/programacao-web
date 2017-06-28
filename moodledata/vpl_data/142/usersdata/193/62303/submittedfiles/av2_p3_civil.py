# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def soma1(h,m):
    mh=media(h)
    mm=media(m)
    soma=0
    for i in range(0,len(h),1):
        soma=soma+((h[i]-mh)*(m[i]-mm))
        return(soma)

    a = []
    for i in range(0,n,1):
        valor = float(input('Digite um valor: '))
        a.append(valor)
    return (a)

n = int(input('Digite o tamanho da lista: '))
h = entradaLista(n)
m = entradaLista(n)

p = #CALCULE O VALOR DE P

p =soma 1(h,m)/(soma2(h)*soma2(m))**0.5
p=abs(p)

print('%.4f' % p)
