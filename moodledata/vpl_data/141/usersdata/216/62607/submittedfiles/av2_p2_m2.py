# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de salas:'))
a=[]
for i in range(0,n,1):
    x=int(input('Digite a quantidade de vidas:'))
    a.append(x)

def entrada(a,x):
    for i in range(0,len(a),1):
        if i==x:
            return(i)
            
def somatorio(a,x,y):
    e=entrada(a,x)
    i=e
    while i<y:
        soma=soma+a[i]
        i=i+1
    return(soma)
        
        
    

x=int(input('Digite a entrada:'))
y=int(input('Digite a saida:'))   
print(a)
print(somatorio(a,x,y))
