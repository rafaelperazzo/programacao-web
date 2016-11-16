# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>=lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
def dcrescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<=lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
def igual (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False
#entradas
n=input("Insira a Quantidade de Elemento das Listas: ")
a=[]
b=[]
c=[]
for j in range(0,n,1):
    a.append("Insira um Elemento de a: ")
for k in range(0,n,1):
    b.append("Insira um Elemento de b: ")
for l in range(0,n,1):
    c.append("Insira um Elemento de c: ")
#saidas a
if crescente(a):
    print "S"
else:
    print "N"
if dcrescente(a):
    print "S"
else:
    print "N"
if igual(a):
    print "S"
else:
    print "N"
#saidas b
if crescente(b):
    print "S"
else:
    print "N"
if dcrescente(b):
    print "S"
else:
    print "N"
if igual(b):
    print "S"
else:
    print "N"
#saidas c
if crescente(c):
    print "S"
else:
    print "N"
if dcrescente(c):
    print "S"
else:
    print "N"
if igual(c):
    print "S"
else:
    print "N"