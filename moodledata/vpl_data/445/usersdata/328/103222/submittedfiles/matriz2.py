# -*- coding: utf-8 -*-
n=int(input('Digite a dimensão da matriz:'))
m=[ ]
for i in range(0,n,1):
    v=[ ]
    for j in range(0,n,1):
        v.append(float(input('Digite:')))
    m.append(v)
s1=[ ]
for i in range(0,n,1):
    s1.append(sum(m[i]))
s2=0
for i in range(0,n,1):
    s2+=m[i][i]
if sum(s1)/n==s2:
    print('S')
else:
    print('N')
    