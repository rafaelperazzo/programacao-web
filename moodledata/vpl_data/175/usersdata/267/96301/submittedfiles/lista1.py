# -*- coding: utf-8 -*-

n=int(input('Tamanho da lista: '))
a=[]
par=[]
impar=[]
somaPar=0
contPar=0
somaImpar=0
contImpar=0
for i in range(0,n,1):
    a.append(int(input('Digite o elemento: ')))
for i in range(1,len(a),1):
    if a[i]%2==0:
        somaPar=somaPar+a[i]
        contPar=contPar+1
    else:
        somaImpar=somaImpar+a[i]
        contImpar=contImpar+1
print('Par: ')
print (somaPar)
print(contPar)
print()
print(somaImpar)
print(contImpar)



