# -*- coding: utf-8 -*-
a= []
def crescente(a):
    cont=0
    for i in range(0,a.index(max(a)),1):
        if i==0:
            if a[i]<a[i+1]:
                cont=cont+1
        elif i==a.index(max(a))-1):
            if (a[a.index(max(a))-2]<a[a.index(max(a))-1]):
                cont=cont+1
        else:
            if (a[i-1]<a[i]<a[i+1]):
                cont=cont+1
    if cont==a.index(max(a)):
        return True
    else:
        return False
                
def decrescente(a):
    cont=0
    for i in range(a.index(max(a))+1,len(a),1):
        if i==0:
            if a[i]>a[i+1]:
                cont=cont+1
        elif i==(len(a)-1):
            if (a[len(a)-2]>a[len(a)-1]):
                cont=cont+1
        else:
            if (a[i-1]>a[i]>a[i+1]):
                cont=cont+1
    if cont==a.index(len(a))-a.index(max(a)):
        return True
    else:
        return False
        
        
def pico(a):
    if crescente(a) and decrescente(a):
        print('S')
    else:
        print('N')

    
   
    


n = int(input('Digite a quantidade de elementos da lista: '))


for i in range (0,n,1):
    valor_a= float(input('Digite o elemento da lista: '))
    a.append (valor_a)
    





