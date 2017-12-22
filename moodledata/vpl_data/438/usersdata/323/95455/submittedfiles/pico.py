# -*- coding: utf-8 -*-
'''
def crescente(a):
    cont=0
    for i in range(0,len(a),1):
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
        return True
    else:
        return False
                
def decrescente(a):
    cont=0
    for i in range(0,len(a),1):
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
        return True
    else:
        return False
        
        
def maiorNumero(a):
    for i in range(0,len(a),1):
        if 
    
   
    
'''

n = int(input('Digite a quantidade de elementos da lista: '))

a= []
for i in range (0,n,1):
    valor_a= float(input('Digite o elemento da lista: '))
    a.append (valor_a)
    
if 


