# -*- coding: utf-8 -*-

def media(n):
    soma = 0
    for i in range(0,len(n),1):
        soma = soma + n[i]
    media = soma/len(n)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def somaA(x,y):
    mx=media(x)
    my=media(y)
    soma=0
    for i in range(0,len(x),1):
        soma=soma+((x[i]-mx)*(y[i])-my)
    return(soma)
  
def entradaLista(q):
    x = []
    for i in range(0,q,1):
        valor = float(input('Digite um valor: '))
        x.append(valor)
    return (x)

q = int(input('Digite o tamanho da lista: '))
x = entradaLista(q)
y = entradaLista(q)

p =somaA(x,y)/((somaD(x)*somad(y)**(0,5))

p = abs(p)

print('%.4f' % p)
