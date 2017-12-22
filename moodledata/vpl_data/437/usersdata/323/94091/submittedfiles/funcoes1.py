# -*- coding: utf-8 -*-

n = int(input('Digite a quantidade de termos:'))

a = []
b = []
c = []

for i in range (0,n,1):
    valor_a = float(input('Digite o elemento da lista primeira lista:'))
    a.append (valor_a)
    
for i in range (0,n,1):
    valor_b = float(input('Digite o elemento da lista segunda lista:'))
    b.append (valor_b)    

for i in range (0,n,1):
    valor_c = float(input('Digite o elemento da lista terceira lista:'))
    c.append (valor_c)   

def crescente (a):
    cont=0
    for i in range (0,len(a),1):
    
        if a[i+1]>a[i]:
            cont=cont+1
            return (True)
        else: 
            return (False)

def decrescente (a):
    for i in range (0,len(a),1):
        if a[i+1]<a[i]:
            return (True)
        else: 
            return (False)

def consec_iguais (a):
    for i in range (0, len (a),1):
        if a[i+1]==a[i]:
            return (True)
        else:
            return (False)

if crescente (a):
    print ('S')
else:
    print ('N')
    
if decrescente (a):
    print ('S')
else:
    print ('N')

if consec_iguais (a):
    print ('S')
else:
    print ('N')
    
if crescente (b):
    print ('S')
else:
    print ('N')
    
if decrescente (b):
    print ('S')
else:
    print ('N')

if consec_iguais (b):
    print ('S')
else:
    print ('N')
    
if crescente (c):
    print ('S')
else:
    print ('N')
    
if decrescente (c):
    print ('S')
else:
    print ('N')

if consec_iguais (c):
    print ('S')
else:
    print ('N')