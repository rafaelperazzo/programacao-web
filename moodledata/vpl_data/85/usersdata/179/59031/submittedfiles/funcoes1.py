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
    b.append(input('digite B - %dº valor :'%i))
for i in range(0,n,1):
    c.append(input('digite C - %dº valor :'%i))
for i in range(0,n,1):
    d.append(input('digite D - %dº valor :'%i))
def teste(a):
    if crescente (b):
        print('S')
    else:
        print('N')
    if decrescente (c):
        print('S')
    else:
        print('N')
    if consecutivo (d):
        print('S')
    else:
        print('N')
teste(b)        
teste(c)
teste(d)









#escreva as demais funções





#escreva o programa principal
