# -*- coding: utf-8 -*-

def crescente (a):
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i]<a[i+1]:
            cont=cont+1
    if cont==len(a)-1:
        return True
    else:
        return False
        
def decrescente (a):
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            cont=cont+1
    if cont==len(a)-1:
        return True
    else:
        return False
        
def consecutivo (a):
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i]==a[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False
n=int(input('digite o valor de n :'))        
b=[]
c=[]
d=[]
for i in range(0,n,1):
    valor=int(input('digite o valor :'))
    b.append(valor)
if crescente (b):
    print('S')
else:
    print('N')
for i in range(0,n,1):
    valor=int(input('digite o valor :'))
    c.append(valor)
if decrescente(c):
    print('S')
else:
    print('N')
for i in range(0,n,1):
    valor=int(input('digite o valor :'))
    d.append(valor)
if consecultivo(d):
    print('S')
else:
    print('N')    














#escreva as demais funções





#escreva o programa principal
