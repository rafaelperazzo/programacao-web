# -*- coding: utf-8 -*-
valores=(int(input('Digite a quatidade de valores:')))
a= []
contpar=0
contimpar=0
somapar=0
somaimpar=0


for i in range (0,valores,1):
    a.append(int(input('DIGITE UM NUMERO:')))
    
for i in range (0,valores,1):
    if a[i]%2==0:
        contpar+=1
        somapar+=a[i]
    else:
        contimpar+=1
        somaimpar+=a[i]
print(somaimpar)
print(somapar)
print(contimpar)
print(contpar)
print(a)


