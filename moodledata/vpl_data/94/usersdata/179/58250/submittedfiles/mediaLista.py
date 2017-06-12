# -*- coding: utf-8 -*-
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return(resultado)
n=int(input('digite o valor de n :'))
a=[]
x=0
z=0
for i in range(0,n,1):
    valor=int(input('digite o valçor do numero :'))
    a.append(valor)
    if i==0:
        x=valor
    if i==(n-1):
        z=valor
print('%.2f'%x)
print('%.2f'%z)
print('%.2f'%media(a))
print(a)
        


