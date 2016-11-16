# -*- coding: utf-8 -*-
from __future__ import division

def crescente(a):
    cont=0
    for i in range (0,len(a),1):
        if i==0:
            if a[0]<a[1]:
                cont=cont+1
        elif i==(len(a)-1):
            if a[len(a)-1]>a[len(a)-2]:
                cont=cont+1
    if cont==(len(a)):
        return True
    else:
        return False
        
def decrescente(a):
    cont=0
    for i in range (0,len(a),1):
        if i==0:
            if a[0]>a[1]:
                cont=cont+1
        elif i==(len(a)-1):
            if a[len(a)-1]<a[len9a0-2]:
                cont=cont+1
        else:
            if a[i]<a[i-1] and a[i]>a[i+1]:
                cont=cont+1
    if cont==(len(a)):
        return True
    else:
        return False
        
def consecutivos(a):
    
        
        
        
        
        
        
        
        
        
        
        a[i]<=[i+1]:
            cont=cont+1
    if cont==0 and posicao!=0:
        return True
    else:
        return False
        
def decrescente(a):
    cont=0
    for i in range (posicao, len(a)-1,1):
        if a[i]>=[i+1]:
            cont=cont+1
    if cont==0 and posicao!=0:
        return True
    else:
        return False
        
def consecutivos(a):
    
        
