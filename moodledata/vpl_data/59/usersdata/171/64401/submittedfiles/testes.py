# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
def numfeliz(n):
    a=[]
    while n>0:
        if n>=10:
            digito=n%10
            a.append(digito)
        else:
            a.append(n)
        n=n//10
    return(a)
def soma(a):
    soma=0
    for i in range(0,len(a),1):
        while soma !=1:
            soma=soma+((a[i])**2)
            x=numfeliz(soma)
            if x==1:
                break
        if x==1:
            return True
        else:
            return False
n=int(input('digite numero:'))
a=[]
if numfeliz(n):
    if soma(a):
        print('S')
    else:
        print('N')