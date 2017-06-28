# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def numerador(x,y):
    for i in range(0,len(x),1):
        soma=0
        c=media(x)
        d=media(y)
        soma=soma+((x[i]-c)*(y[i]-d))
    return(soma)
    
def denominador(x):
    for i in range(0,len(x),1):
        soma=0
        c=media(x)
        soma=soma+((x[i]-c))**2
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

j=numerador(x,y)
t=denominador(x)
r=denominador(y)
p = (j)/((t*r)**(0.5))

p = abs(p)

print('%.4f' % p)
