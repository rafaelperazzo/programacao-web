# -*- coding: utf-8 -*-
def modulo(h):
    if h<0:
        h=(-1)*h
    return h

while True:
    n=float(input('Digte um número: '))
    print(modulo(n))