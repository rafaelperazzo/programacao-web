# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def somaA(x,y):
    mx=media(x)
    my=media(y)
    soma=0
    for i in range(0,len(x),1):
        soma=soma+((x[i]-mx)*(y[i]-my))
    return(soma)
    
def somaD(x):
    mx=media(x)
    for i in range(0,len(x),1):
        soma=soma+(x[i]-mx)
    return(soma)
    
def somaD(y):
    for i in range(0,len(y),1):
        soma=soma+(y[i]-my)
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

p = #CALCULE O VALOR DE P

p = somaA(x,y)/((somaD(x)*somaD(y))**(1/2))

print('%.4f' % p)
