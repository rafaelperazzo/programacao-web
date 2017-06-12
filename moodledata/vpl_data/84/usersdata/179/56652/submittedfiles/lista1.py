# -*- coding: utf-8 -*-
def somatorio(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            soma=soma+a[i]
    return(soma)

def somatorio(b):
    soma=0
    for i in range(0,len(b),1):
        if b[i]%2==0:
            soma=soma+b[i]
    return(soma)
    
def quantidade(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            cont=cont+a[i]
    return(cont)
    
def quantidade(b):
    cont=0
    for i in range(0,len(b),1):
        if b[i]%2==0:
            cont=cont+b[i]
    return(cont)
    
n=int(input('digite o valor de n :'))
x=[]
for i in range(1,n+1,1):
    lista=float(input('digite o valor da lista :'))
    x.append(lista)
print(somatorio(x))
print(somatorio(x))
print(quantidade(x))
print(quantidade(x))













    


