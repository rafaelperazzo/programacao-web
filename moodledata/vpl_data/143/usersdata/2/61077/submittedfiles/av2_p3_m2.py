# -*- coding: utf-8 -*-

def entradaLista(n):
    a = []
    for i in range(0,n,1):
        valor = float(input('Digite um valor: '))
        a.append(valor)
    return (a)
    
n = int(input('Digite um valor: '))
a = entradaLista(n)


