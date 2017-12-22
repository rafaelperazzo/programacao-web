# -*- coding: utf-8 -*-
valores=int(input('DIGITE A QUANTIDADE DE VALORES:'))
e=[]
contpar=0
contimpar=0
somapar=0
somaimpar=0
for i in range (0,valores,1):
    e.append(int(input('DIGITE UM NUMERO:')))
for i in range (0,valores,1):
    if e[i]%2==0:
        contpar+=1
        somapar+=[e]
    else:
        contimpar+=1
        somaimpar+=[e]
print(somaimpar)
print(somapar)
print(contimpar)
print(contpar)
print(e)

