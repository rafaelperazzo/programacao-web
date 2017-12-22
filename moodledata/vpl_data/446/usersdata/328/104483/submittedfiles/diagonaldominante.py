# -*- coding: utf-8 -*-
d=int(input ('Digite a ordem da matriz:'))
l=[]
m=[]
for i in range(d):
    l.append(int(input('Dê valores a matriz:')))
    m=m+i
    for j in range(d):
        m.append(l)
print(m)

    

