# -*- coding: utf-8 -*-
from __future__ import division

n = input("Digite n:")
a = []
b = []
c = []

for i in range (0, n, 1):
    a.append(input("Digite um elemento:"))
for i in range (0, n, 1):
    b.append(input("Digite um elemento:"))
for i in range (0, n, 1):
    c.append(input("Digite um elemento:"))


def crescente (a):
    cont = 0
    if i == 0:
        if a[i] < a[i + 1]:
        cont = cont +1
    if cont == a[len(a) - 1]:
        return S
    else:
        return N
def crescente (b):
    cont = 0
    if i == 0:
        if b[i] < b[i + 1]:
        cont = cont +1
    if cont == b[len(b) - 1]:
        return S
    else:
        return N
def crescente (c):
    cont = 0
    if i == 0:
        if c[i] < c[i + 1]:
        cont = cont +1
    if cont == c[len(c) - 1]:
        return S
    else:
        return N
        
def decrescente (a):
    cont = 0
    if i == 0:
        if a[i] > a[i + 1]:
        cont = cont +1
    if cont == a[len(a) - 1]:
        return S
    else:
        return N
        
def decrescente (b):
    cont = 0
    if i == 0:
        if b[i] > b[i + 1]:
        cont = cont +1
    if cont == b[len(b) - 1]:
        return S
    else:
        return N

def decrescente (c):
    cont = 0
    if i == 0:
        if c[i] > c[i + 1]:
        cont = cont +1
    if cont == c[len(c) - 1]:
        return S
    else:
        return N


def igualdade (a):
    cont = 0
    if i == 0:
        if a[i] == a[i + 1]:
        cont = cont +1
    if cont == a[len(a) - 1]:
        return S
    else:
        return N

def igualdade (b):
    cont = 0
    if i == 0:
        if b[i] == b[i + 1]:
        cont = cont +1
    if cont == b[len(b) - 1]:
        return S
    else:
        return N

def igualdade (c):
    cont = 0
    if i == 0:
        if c[i] == c[i + 1]:
        cont = cont +1
    if cont == c[len(c) - 1]:
        return S
    else:
        return N
