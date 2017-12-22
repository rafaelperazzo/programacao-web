# -*- coding: utf-8 -*-

def modulo (a):
    if a>0:
        a = a
    else:
        a = -a
        
    return (a)
    
n = int (input('Digite a quantidade de elementos da lista: '))

a = []

for i in range (0,n,1):
    valor = float(input('Digite o elemento: '))
    a.append (valor)

degraus = [] 

for i in range (0,n,1):
    diferenca = a[i+1]-a[i]
    degrau = modulo (diferenca)
    degraus.append (degrau)
    
print (max (degraus))