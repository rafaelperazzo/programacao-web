# -*- coding: utf-8 -*-
n = int(input('Digite a dimensão da matriz quadrada: '))

matriz = []
for i in range(0,n,1):
    a = []
    for j in range(0,n,1):
        a.append(float(input('digite:')))
    matriz.append(a)
    
        
s1 = []
for i in range(0,n,1):
    s1.append(sum(matriz[i]))
    
s2 = 0
for i in range(0,n,1):
    s2 = s2+matriz[i][i]

if sum((s1)/n) == 2:
    print ('S')
else:
    print ('N')




    

