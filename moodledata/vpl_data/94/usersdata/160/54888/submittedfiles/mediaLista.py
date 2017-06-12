# -*- coding: utf-8 -*-


def media(n):
    soma=0
    for i in range(0,len(n),1):
        soma=soma+n[i]
    resultado=soma/len(n)
    return (resultado)
    

n=int(input('Digite a quantidade:'))
a=[]
for i in range(0,n,1):
    valor=float(input('Digite:'))
    a.append(valor)
print('%.2f'%(a[0]))
print('%.2f'%(a[i]))
print('%.2f'%media(a))
print('%.2f'%a)