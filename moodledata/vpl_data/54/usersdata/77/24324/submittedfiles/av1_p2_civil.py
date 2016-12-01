# -*- coding: utf-8 -*-
from __future__ import division


a=[]
n=int(input('Digite a quantidade de pinos presentes na fechadura:'))
m=int(input('Digite a altura padrão para todos os pinos:'))

for i in range(0,n,1):
    a.append(input('Acrescente valores a lista:'))
    

 
def valor_absoluto(x):
    if x<0:
        x=x*(-1)
    return x
    
    else:
    
    return x 
        
        

def pinoMaior(a):
    maior=a[0]
    for i in range(0,len(a),1):
        if a[i]>maior:
            maior=a[i]
        
        return pinomaior

    
def pinoMenor(a):
    menor=a[0]
    for i in range(0,len(a),1):
        if a[i]<menor:
            menor=a[i]
        
        return menor


    
def altura(a,altura):
    soma=valor_absoluto(pinoMaior(a)-altura)+valor_absoluto(pinoMenor(a)-altura)
    return soma
    

print('%d' %(altura(a,m)))
    
    
