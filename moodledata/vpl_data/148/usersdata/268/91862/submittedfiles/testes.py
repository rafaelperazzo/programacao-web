# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n '))
a=[]
multiplicacao=1
for i in range(0,n,1):
    valor=int(input('Digite o valor'))
    a.append(valor)
for i in range(0,len(a),1):
    multiplicacao= multiplicacao*a[i]
resultado = multiplicacao**(1/len(a))
print(resultado)  