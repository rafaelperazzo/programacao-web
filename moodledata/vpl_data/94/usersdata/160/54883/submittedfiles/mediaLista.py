# -*- coding: utf-8 -*-


def media(n):
    soma=0
    for i in range(0,len(n),1):
        soma=soma+n[i]
    resultado=soma/len(n)
    return (resultado)
    
a=[]
n=int(input('Digite a quantidade:'))
for i in range(1,n,1):
    valor=int(input('Digite:'))
    a.append(valor)
print('%.2f'%a[0])
print('%.2f'%a[i])
print('%.2f'%media(a))
print(a)