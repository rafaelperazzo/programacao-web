# -*- coding: utf-8 -*-
def lista(a,b):
    for i in range(0,b,1):
        a.append(int(input('digite: ')))






n = int(input('digite quantidade de a: '))
m = int(input('digite quantidade de b: '))
a = []
b = []
som = 0
for i in range(0,n,1):
    a.append(int(input('digite a: ')))

for i in range(0,m,1):
    b.append(int(input('digite b: ')))

for i in range(0,m,1):
    if b[i] in a:
        som+=1
        
print (som)


