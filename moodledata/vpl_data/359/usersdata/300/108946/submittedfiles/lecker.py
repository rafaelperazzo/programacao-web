# -*- coding: utf-8 -*-
n = int(input('Digite o número de elementos nas listas: '))
a = []
b = []
for i in range(0,n,1):
    a.append(int(input('Digite um elemento de a: ')))
for i in range(0,n,1):
    b.append(int(input('Digite um elemento de b: ')))

def lecker(a):
    cont = 0
    if a[0] < a[1] and a[len(a) - 1] < a[len(a) - 2]:
        p = 0
        h = 0
        for i in range(1,len(a),1):
            if a[i] > a[i] - 1:
                p = a[i]
                h = 0
        if p > a[h-1] and p > a[h+1]:
            return True
        else:
            return False
    else:
        return False
        
if lecker(a):
    print ('S')
else:
    print ('N')
if lecker(b):
    print ('S')
else:
    print ('N')    
    
        
    

