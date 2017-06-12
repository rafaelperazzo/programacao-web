# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvpadrao(lista,media):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((a[i]-media)**2)
    desvpadrao=((soma/(n-1))**0.5
    return desvpadrao
n=int(input('tamanho da lista a:'))
a=[]
for i in range(