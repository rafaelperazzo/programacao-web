# -*- coding: utf-8 -*-
import itertools
def each_cons(xs, n):
    return itertools.izip(*(xs[i:] for i in xrange(n)))


a=[]
n=int(input('Digite a quantidade de termos da sequência: '))
for i in range(0,n,1):
    valor_a=float(input('Digite um elemento da sequência: '))
    a.append(valor_a)
degrau= [(a-b) for a, b in each_cons(a,2)]
print(degrau)
