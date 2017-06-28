# -*- coding: utf-8 -*-
import numpy as np      

def MaGiCa(matriz):
    sp=0
    ss=0
    st=0
    for i in range (0,matriz.shape[0],1):
        st=st+matriz[i,2]
        ss=ss+matriz[i,1]
        sp=sp+matriz[i,0]
        if sp==ss:
            x=sp
        else:
            x=st
        return(x)
def mudar_linha (matriz,x):
    lista=[]
    for i in range (0,matriz,shape[0],1):
        soma=0
        for j in range (0,matriz,shape[1],1):
            soma=soma+matriz[i,j]
            lista.append(soma)
        for i in range (0,len(lista),1):
            soma=0
            if lista[i]!=x:
                return i
def mudar_coluna (matriz,x):
    lista=[]
    for i in range(0,matriz.shape[1],1):
        soma=soma+matriz[i,j]
    lista.append(soma)
for j in range (0,len(lista),1):
    if lista [i]!=x:
        j=i
        return j
def valor_correto (matriz,linha,coluna,x):
    s1=0
    s2=0
    for i in range (0,matriz.shape[0],1):
        s2=s1+matriz[i,coluna]
    for j in range(0,matriz.shape[1],1):
        s2=s2+matriz[linha,j]
        g=s1+s2-(2*matriz[linha,coluna])
        total=x-(g/2)
        return total
d= int(input("digite a dimensão da matriz"))
matriz=np.zeros( (d,d) )
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=int(input("digite o valor do elemento"))
x=x(matriz)
linha=mudar_linha(matriz,x)
coluna=mudar_coluna(matriz,x)
valor_total=valor_correto(matriz,linha,coluna,x)
print("%.f" %matriz[linha,coluna])
print("%.f" %valor_total)

    



