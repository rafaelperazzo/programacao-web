# -*- coding: utf-8 -*-

n= int(input('Digite a quantidade de elementos da lista:'))

a=[]

QP:0
QI=
SP=0
SI=0
for i in range(1,n+1,1):
    valor=int(input('Valor da lista:'))
    a.append(valor)
for j in range(0, len(a), 1):
    if (a[j]%2==0):
        QP= QP+1
        SP=SP+ a[j]
    else:
        QI=QI+1
        SI=SI+a[j]
print(SI)
print(SP)
print(QP)
print(QI)
print(a)
        
    







































































