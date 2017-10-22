# -*- coding: utf-8 -*-
while(True):
    while(True):
        n=int(input('digite um numero positivo: '))
        if (n>=0):
            break
    f=1
    for i in range(2,n+1,1):
        f*=i
    print('%d!=%d' % (n,f))









#defina a função
def fatorial(n):
    f=1
    for i in range(2,n+1,1):
        f*=1
    return f
#vou usar
while(True):
    while(True):
        n=int(input('digite um numero positivo: '))
        if (n>=0):
            break
    f=fatorial(n)
    print('%d!=%d' % (n,f))

    
    
        