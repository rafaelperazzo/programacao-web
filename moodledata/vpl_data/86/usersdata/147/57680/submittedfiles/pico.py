# -*- coding: utf-8 -*-

def pico(lista):
n =int(input('Digite a quantidade de elementos da lista:'))

before=int(input('digite n before:'))
now=int(input('digite n now:'))

numpicos=0
numvales=0

i=2
while i<n:
    after=int(input('digite n after:'))
    if before<now>after:
        numpicos=numpicos+1
    elif before>now<after:
        numvales=numvales+1
    before=now
    now=after
    i=i+1
if numpicos==1 and numvales==0:
    print('S')
else:
    print('N')