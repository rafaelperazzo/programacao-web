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
    cont = 0
    for i in range (0,len(a),1):
        if i==0:
            if a[i]<a[i+1]:
                cont=cont+1
        elif i==(len(a)-1):
            if (a[len(a)-2]<a[len(a)-1]):
                cont=cont+1
        else:
            if (a[i-1]<a[i]<a[i+1]):
                cont=cont+1
    if cont==len(a):
        return (True)
    else:
        return (False)
        
def decrescente (a):
    cont = 0
    for i in range (0,len(a),1):
        if i==0:
            if a[i]>a[i+1]:
                cont=cont+1
        elif i==(len(a)-1):
            if (a[len(a)-2]>a[len(a)-1]):
                cont=cont+1
        else:
            if (a[i-1]>a[i]>a[i+1]):
                cont=cont+1
    if cont==len(a):
        return (True)
    else:
        return (False)
    

def consec_iguais (a):
    cont = 0
    for i in range (0,len(a),1):
        if i==0:
            if a[i]==a[i+1]:
                cont=cont+1
        elif i==(len(a)-1):
            if (a[i-1]==a[i]):
                cont=cont+1
        else:
            if (a[i]==a[i+1]):
                cont=cont+1
    if cont!=0:
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