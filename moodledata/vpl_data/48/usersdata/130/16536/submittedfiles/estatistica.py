# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
a=[]
b=[]
n=input('Digite o valor de n:')
for i in range(0,n,1):
    a.append(input('Digite um elemento de a:'))
for i in range(0,n,1):
    b.append(input('Digite um elemento de b:'))
Ma=media(a)
Mb=media(b)
sa=0
i=0
while i<n:
    sa=sa+(a[i]-Ma)**2
Da=sa/(len(a)-1)
print('%.2f'%Ma)
print('%.2f'%Da)
sb=0
i=0
while i<n:
    sb=sb+(b[i]-Mb)**2
Db=sb/(len(b)-1)
print('%.2f'%Db)
print('%.2f'%Mb)    


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 