# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n = int(input('Digite a quantidade de termos:'))

a = []

for i in range (0,n,1):
    x = float(input('Digite o valor:'))
    a.append (x)

def crescente (a):
    for i in range (0,len(a),1):
        if a[i+1] > a[i]:
            return (True)
        else:
            return (False)

def decrescente (a):
    for i in range (0,len(a),1):
        if a[i+1] < a[i]:
            return (True)
        else:
            return (False)
   
if crescente (a):
    print ('crescente')
elif decrescente (a):
    print ('decrescente')
else:
    print ('n')
    