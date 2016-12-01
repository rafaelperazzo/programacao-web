# -*- coding: utf-8 -*-
from __future__ import division


                                                                                #ENTRADA
#----------------------------------------------------------------------------------------------------------------------------------
a=[]
n=int(input('Digite a quantidade de pinos presentes na fechadura:'))
m=int(input('Digite a altura padrão para todos os pinos:'))

for i in range(0,n,1):
    a.append(input('Acrescente valores a lista:'))





                                                                                #FUNÇÕES
#----------------------------------------------------------------------------------------------------------------------------------    
def pinoMaior(a):
    pinomaior=a[0]
    for i in range(0,len(a),1):
        if a[i]>pinomaior:
            pinomaior=a[i]
        
        return pinomaior
        
def pinoMenor(a):
    pinomenor=a[0]
    for i in range(0,len(a),1):
        if a[i]<pinomenor:
            pinomenor=a[i]
        
        return pinomenor


def valor_absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
    
def altura(a,m):
    soma=valor_absoluto(pinoMaior(a)-m)+valor_absoluto(pinoMenor(a)-m)
    return soma
    

                                                                                #SAÍDA
#----------------------------------------------------------------------------------------------------------------------------------    
print('%d' %altura(a,m))