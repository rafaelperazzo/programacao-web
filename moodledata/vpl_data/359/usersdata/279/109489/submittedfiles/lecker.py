# -*- coding: utf-8 -*-
n=(int(input()))
lista1=[]
lista2=[]     
for i in range(0,n,1) :
   lista1.append(int(input()))
   
for i in range(0,n,1) :
   lista2.append(int(input()))    

def verifica(lista) :
    a=0
    s=0
    f=0
    for i in range(0,n-1,1):
        if lista[i]>lista[i+1] :
            s=i
            break  
    if s>0 :        
      for i in range(s,n-1,1):    
         if lista[i]<lista[i+1] :
             f=i
    if f==0 and s>0 :
        return True
    else:
        return False
if verifica(lista1):
    print('S')
else:
    print('N')
if verifica(lista2):
    print('S')
else:
    print('N') 








































