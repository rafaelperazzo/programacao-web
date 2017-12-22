# -*- coding: utf-8 -*-
n=int(input('Digite a ordem da matriz: '))
a=[]
for i in range (n):
    b=[]
    for j in range(n):
        b.append(int(input('Digite o valor%d %' ((i+1),(i+j)))))
    a.append(b)

    
