# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    media = soma/len(a)
    return (media)

#ESCREVA AS DEMAIS FUNÇÕES
  
def soma1(x,y):
    mx=media(x)
    my=media(y)
    soma=0
    for i in range(0,len(x),1):
        soma=soma+((x[i]-mx)*(y[i]-my))
    return(soma)
    
def soma2(lista):
    L=media(lista)
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-L)**2
    return(soma)
    
def entradaLista(n):
    a=[]
    for i in range(0,n,1):
        valor+float(input('Digite um valor: '))
        a.append(valor)
    return(a)
    
n=int(input('Digite o tamanho da lista: '))
x=entradalista(n)
y=entradaLISTA(n)

p=soma1(x,y)/(soma2(y))**0.5

p=abs(p)