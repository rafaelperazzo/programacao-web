# -*- coding: utf-8 -*-
from __future__ import division

def crescente(x):
    for i in range (0,len(x)-1,1):
        if x[i] > x[i + 1]:
            return False
        else:
            return True
        
def decrescente(x):
    for i in range (0,len(x)-1,1):
        if x[i] < x[i + 1]:
            return False
        else:
            return True
            
def elemconsec(x):
    for i in range (0,len(x)-1,1):
        if x[i] == x[i + 1]:
            return True
        else:
            return False
            

#escreva o programa principal

n = input('Digite a quantidade de elementos:')
a = []
b = []
c = []

for i in range (0,n,1):
    a.append(input('Digite o elemento de a:'))
print a
for i in range (0,n,1):
    b.append(input('Digite o elemento de b:'))
print b
for i in range (0,n,1):
    c.append(input('Digite o elemento de c:'))
print c

if crescente(a,b,c):
    print 'S'
else:
    print 'N'
if decrescente(a,b,c):
    print 'S'
else:
    print 'N'
if elemconsec(a,b,c):
    print 'S'
else:
    print 'N'


    
   
   
