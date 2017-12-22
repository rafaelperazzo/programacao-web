# -*- coding: utf-8 -*-

def modulo (a):
    if a>0:
        a = a
    else:
        a = -a
        
    return (a)
    
n = int (input('Digite a quantidade de elementos da lista: '))

while (n<2):
    n = int (input('Digite a quantidade de elementos da lista: '))

a = []

for i in range (0,n,1):
    valor = int(input('Digite o elemento: '))
    a.append (valor)

degraus = [] 

for i in range (0,n,1):
    if i == 0:
        diferenca = diferenca = a[1]-a[0]
    elif i == len(a):
        diferenca = diferenca = a[len(a)-1]-a[len(a)-2]
    else:
        diferenca = diferenca = a[i]-a[i-1]
    degrau = modulo (diferenca)
    degraus.append (degrau)
    
print (max (degraus))