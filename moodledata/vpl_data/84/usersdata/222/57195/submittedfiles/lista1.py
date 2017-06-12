# -*- coding: utf-8 -*-
n=int(input('n:'))
lista=[]
impares=[]
pares=[]
somaImpares=0
somaPares=0
for i in range(1,n+1,1):
    a=int(input('a:'))
    lista=lista+[a]
for numero in  lista:
    if numero%2==1:
        impares=impares+[numero]
        somaImpares=somaImpares+numero
    elif numero%2==0:
        pares=pares+[numero]
        somaPares=somaPares+numero
lista.sort()
qtdimpares=len(impares)
qtdpares=len(pares)
print(somaImpares)
print(somaPares)
print(qtdimpares)
print(qtdpares)
print(lista)


