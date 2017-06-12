# -*- coding: utf-8 -*-
def média(a):
    soma=0
    for j in range(0,len(a),1):
        soma=soma+a[j]
    média=soma/len(a)
    return média

n=int(input('Digite a Quantidade de Números:'))
l1=[]
for i in range(1,n+1,1):
    v=float(input('Digite o Valores de Inteiros da Lista:'))
    l1.append(v)
print('%.2f' %l1[0])
print('%.2f' %l1[len(l1)-1])
print('%.2f' %média(l1))
print(l1)




