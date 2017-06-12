# -*- coding: utf-8 -*-


def media(a):
    soma=o
    for i in range(0,len(a),1):
        soma=soma+a[i]
    resultado=soma/len(a)
    return (resultado)
    
a=[]
n=int(input('Digite a quantidade:'))
for i in range(1,n+1,1):
    idade=int(input('Digite:'))
    a.append(idade)
print('%.2f'%a[0])
print('%.2f'%a[i])
print('%.2f'%media(a))
print(a)