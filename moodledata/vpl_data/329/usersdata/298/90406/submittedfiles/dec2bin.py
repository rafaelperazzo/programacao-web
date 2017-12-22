# -*- coding: utf-8 -*-
def algarismos(n):
    alg=1
    while(n//10)>0:
        n=n//10
        alg=alg+1
    return alg

p = int(input('Digite o número p: '))
q = int(input('Digite o número q: '))

if algarismos(p)<=algarismos(q):
    
if algarismos(p)>algarismos(q):
    print('N')