# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desviopadrao(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-resultado)**2)
    d=((1/(n-1))*soma)**0.5
    return d

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
a=[]
b=[]
n=int(input('Digite o número de elementos da lista:'))


def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    resultado=soma/len(a)
    return resultadoa
def desviopadrao(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+((a[i]-resultadoa)**2)
    da=((1/(n-1))*soma)**0.5
    return da
    
def media(b):
    soma=0
    for i in range(0,len(b),1):
        soma=soma+b[i]
    resultado=soma/len(b)
    return resultadob
def desviopadrao(b):
    soma=0
    for i in range(0,len(b),1):
        soma=soma+((b[i]-resultadob)**2)
    db=((1/(n-1))*soma)**0.5
    return db