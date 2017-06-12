# -*- coding: utf-8 -*-
def somatorio1(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            soma=soma+a[i]
    return(soma)

def somatorio2(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            soma=soma+a[i]
    return(soma)
    
def quantidade1(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            cont=cont+1
    return(cont)
    
def quantidade2(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            cont=cont+1
    return(cont)
def listainteira(a):
    for i in range(0,len(a),1):
        valores==a[i]
    return(valores)    
    
n=int(input('digite o valor de n :'))
x=[]
for i in range(1,n+1,1):
    lista=float(input('digite o valor da lista :'))
    x.append(lista)
print(somatorio1(x))
print(somatorio2(x))
print(quantidade1(x))
print(quantidade2(x))
print(listainteira(x))













    


