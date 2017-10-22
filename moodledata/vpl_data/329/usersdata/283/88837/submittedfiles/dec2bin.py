# -*- coding: utf-8 -*-

a=int(input('a: '))
while (a<0):
    print('Número Inválido')
    break
def h(a):
    j=1
    for i in range(1,a,1):
        z=a//j
        j *= 10 
        if (z==0):
            break
    return z
print(h(a))
    