# -*- coding: utf-8 -*-
from __future__ import division
import math
import numpy as np

#escreva suas funcoes aqui
def erro(A,T):
    soma = 0    
    for i in range(0,A.shape[0],1):
        for j in range(0,A.shape[1],1):
            soma = soma + ((A[i,j]-T[i,j])**2)
    
    resultado = np.sqrt(soma/(A.shape[0]**2))
    return resultado

def calcular_a(A):
    a = []    
    for j in range(0,A.shape[1],1):
        a.append(sum(A[:,j]))
    return a

def calcularOi(A):
    oi = []
    for i in range(0,A.shape[0],1):
        oi.append(sum(A[i,:]))
    return oi
    
def gravitacional(A,d,alfa):
    
    a = calcular_a(A)    
    
    oi = calcularOi(A)
    
    T = np.zeros((A.shape[0],A.shape[1]))
    
    for i in range(0,A.shape[0],1):
        for j in range(0,A.shape[1],1):
            if i!=j:
                soma = 0
                for k in range(0,A.shape[0],1):
                    if d[i,k]!=0:
                        soma = soma + a[k]*(1/(d[i,k]**alfa))
            
                numerador = a[j]*(1/(d[i,j]**alfa))
            
                denominador = soma
            
                T[i,j]=oi[i]*(numerador/denominador)
    
    return T


def procurarAlfa(A,d,minimo,maximo,intervalo=1):
    erros = []
    indices = []
    for alfa in np.arange(minimo,maximo,intervalo):
        T = gravitacional(A,d,alfa)
        erro1 = erro(A,T)
        erros.append(erro1)
        indices.append(alfa)
    T = gravitacional(A,d,indices[erros.index(min(erros))])
    return (min(erros),indices[erros.index(min(erros))],T)
    

def matriz2HTML(a):
    tabela = '<table>\n'    
    for i in range(0,a.shape[0],1):
        tabela = tabela + '<tr>\n'        
        for j in range(0,a.shape[1],1):
            tabela = tabela + '<td>' + str(round(a[i,j],4)) + '</td>'
        tabela = tabela + '\n'
        tabela = tabela + '</tr>\n'
    tabela = tabela + '</table>'
    return tabela