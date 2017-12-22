# -*- coding: utf-8 -*-
a = []
for i in range(1 ,4 ,1):
    a.append(float(input('Digite o elemento : ')))
print(a)
print(sum(a))
print(len(a))
del a[1]
print(a)
print(len(a))
a[2] = 5.0
print(a)

#for i in range(2 , -1 , -1):
#    print(a[i])