# -*- coding: utf-8 -*-

def entradaLista(n):
    a = []
    for i in range(0,n,1):
        valor = int(input('Digite um valor: '))
        a.append(valor)
    return (a)

def calculaDegraus(a):
    degraus = []
    for i in range(0,len(a)-1,1):
        degraus.append(abs(a[i]-a[i+1]))
    return (degraus)
    
n = int(input('Digite um valor: '))
a = entradaLista(n)
print(calculaDegraus(a))




