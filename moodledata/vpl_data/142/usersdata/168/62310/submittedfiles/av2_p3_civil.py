# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
def somaA(a,b):
    mx=media(x)
    my=media(y)
    soma=0
    for i in range (0,len(a),1):
        soma=soma+((x[i]-mx)*(y[i]-my))
    return soma
def somaB(lista):
    mlista=media(lista)
    soma=0
    for i in range (0,len(lista),i):
        soma=soma+(lista[i]-mlista)**2
    return soma
    
  
def entradaLista(n):
    x = []
    for i in range(0,n,1):
        valor = float(input('Digite um valor: '))
        x.append(valor)
    return (x)

n = int(input('Digite o tamanho da lista: '))
x = entradaLista(n)
y = entradaLista(n)

p =somaA(x,y)/((somaB(x)*somaB(y))**(0.5))

p = abs(p)

print('%.4f' % p)
