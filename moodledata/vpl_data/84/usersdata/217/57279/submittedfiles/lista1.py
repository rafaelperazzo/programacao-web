# -*- coding: utf-8 -*-
def qimpar(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            cont=cont+1
    print (cont)

def qpar(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            cont=cont+1
    print (cont)

def simpar(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            soma=soma+a[i]
    print(soma)

def spar(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            soma=soma+a[i]
    print(soma)

n=int(input('digite n:'))

a=[]

for i in range(1,n+1,1):
    a.append(int(input('elementos:'))


simpar(a)
spar(a)
qimpar(a)
qpar(a)
print (a)


