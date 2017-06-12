# -*- coding: utf-8 -*-
def média(a):
    soma=0
    for j in range(0,len(a),1):
        soma=soma+a[j]
    resultado=soma/len(a)
    return resultado 
n=int(input('Digite a Quantidade de Números:'))
l1=[]
for i in range(0,n,1):
    v=float(input('Digite o Valores de Inteiros da Lista:'))
    l1.append(v)
print('%.2f' %l1[0])
print('%.2f' %l1[i])
print('%.2f' %média(l1))
print(l1)




