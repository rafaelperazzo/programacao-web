# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de valores da matriz: '))
a = []
for i in range(0,n,1):
    a.append(int(input('Digite a%d:' %(i+1))))
s = 0
j = 0
for i in range(0,n,1):
    if a[i]%2 != 0:
        s = s + a[i]
print(s)
    elif a[i]%2 ==0:
        j = j + a[i]
 print(j)
        
        




